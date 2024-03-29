import datetime

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone
from authapp.models import Person


class ChatManager(models.Manager):
    use_for_related_fields = True

    def unreaded(self, user=None):
        qs = self.get_queryset().exclude(last_message__isnull=True).filter(last_message__is_read=False)
        return qs.exclude(last_message__author=user) if user else qs


class Chat(models.Model):
    DIALOG = 'D'
    CHAT = 'C'
    CHAT_TYPE_CHOICES = (
        (DIALOG, 'Dialog'),
        (CHAT, 'Chat')
    )

    type = models.CharField(max_length=1, choices=CHAT_TYPE_CHOICES, default=DIALOG, verbose_name='Тип')
    members = models.ManyToManyField(Person, verbose_name="Участник", blank=False)
    title = models.CharField(max_length=50, blank=False, verbose_name='Название')
    image = models.FileField("Изображение", upload_to='chat_logos', null=True, blank=True, default=None)
    last_message = models.ForeignKey('Message', related_name='last_message', null=True, blank=True,
                                     on_delete=models.SET_NULL)
    objects = ChatManager()

    class Meta:
        verbose_name = 'Чаты'
        verbose_name_plural = 'Чаты'
        ordering = ('-last_message',)

    @property
    def get_members(self):
        qs = [user.id for user in self.members.all()]
        return qs

    def __str__(self):
        return f'{self.type} - {self.members.all()}'


class Message(models.Model):
    chat = models.ForeignKey(Chat, verbose_name="Чат", on_delete=models.CASCADE)
    author = models.ForeignKey(Person, verbose_name="Пользователь", on_delete=models.CASCADE)
    message = models.TextField("Сообщение")
    image = models.FileField("Изображение", upload_to='messages', null=True, blank=True, default=None)
    pub_date = models.DateTimeField('Дата сообщения', default=timezone.now)
    is_read = models.BooleanField('Прочитано', default=False)

    class Meta:
        ordering = ('pub_date',)
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'

    def __str__(self):
        return self.message

    @property
    def get_date(self):
        today = datetime.date.today()
        msg_date = self.pub_date

        # same day
        if str(today) == msg_date.strftime('%Y-%m-%d'):
            return msg_date.strftime('%H:%M')
        # same year
        elif str(today.year) == str(msg_date.strftime('%Y')):
            return msg_date.strftime('%d %b')
        # last year or early
        else:
            return msg_date.strftime('%d %b %Y')


@receiver(post_save, sender=Message)
def post_save_comment(sender, instance, created, **kwargs):
    if created:
        instance.chat.last_message = instance
        instance.chat.save(update_fields=['last_message'])
