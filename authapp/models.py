from django.contrib.auth.models import AbstractUser
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

from friendsapp.models import FriendRequests

GENDER_CHOICES = [
    ['male', "Мужской"],
    ['female', "Женский"]
]

GENDER_DICT = {
    'male': "Мужской",
    'female': "Женский"
}

# REL_CHOICES = [
#     ['none', "Не определенно"],
#     ['single', "Холост"],
#     ['in_a_rel', "В отношениях"],
#     ['engaged', "Помолвлен(а)"],
#     ['married', "Женат/Замужем"],
#     ['in_love', "Влюблен(а)"],
#     ['complicated', "Все сложно"],
# ]
#
# REL_DICT = {
#     'none': "Не определенно",
#     'single': "Холост",
#     'in_a_rel': "В отношениях",
#     'engaged': "Помолвлен(а)",
#     'married': "Женат/Замужем",
#     'in_love': "Влюблен(а)",
#     'complicated': "Все сложно",
# }

REL_DICT = {
    0: "Не определенно",
    1: "Холост",
    2: "В отношениях",
    3: "Помолвлен(а)",
    4: "Женат/Замужем",
    5: "Влюблен(а)",
    6: "Все сложно",
}


class Person(AbstractUser):
    # NONE = 'NO'
    # SINGLE = 'SNG'
    # IN_REL = 'REL'
    # ENGAGED = 'ENG'
    # MARRIED = 'MRD'
    # IN_LOVE = 'ILV'
    # COMPLICATED = 'CMP'
    # STATUS_CHOICES = (
    #     (NONE, "Не определенно"),
    #     (SINGLE, "Холост"),
    #     (IN_REL, "В отношениях"),
    #     (ENGAGED, "Помолвлен(а)"),
    #     (MARRIED, "Женат/Замужем"),
    #     (IN_LOVE, "Влюблен(а)"),
    #     (COMPLICATED, "Все сложно"),
    # )

    STATUS_CHOICES = (
        (0, "Не определенно"),
        (1, "Холост"),
        (2, "В отношениях"),
        (3, "Помолвлен(а)"),
        (4, "Женат/Замужем"),
        (5, "Влюблен(а)"),
        (6, "Все сложно"),
    )
    avatar = models.FileField(verbose_name="Аватарка", upload_to='users_avatars', blank=True, default=None)
    phone_number = PhoneNumberField(null=True, blank=True, unique=True)
    bio = models.TextField(max_length=500, blank=True, null=True, verbose_name="О себе")
    city = models.CharField(max_length=30, blank=True, null=True, verbose_name="Город")
    birth_date = models.DateField(null=True, blank=True, verbose_name="Дата рождения")
    gender = models.CharField(max_length=10, verbose_name="Пол", choices=GENDER_CHOICES, default="male")
    relationship = models.IntegerField(verbose_name="Статус отношений", choices=STATUS_CHOICES, default=0)

    @property
    def get_friends(self):
        user = Person.objects.get(pk=self.pk)
        # Все подтвержденные запросы в друзья пользовалю и от него
        all_requests = FriendRequests.objects.filter(status=1, initiator=user) | \
                       FriendRequests.objects.filter(status=1, target=user)

        # Получение pk всех друзей пользователя
        friends_pk = []
        for item in all_requests:
            if item.target == user:
                friends_pk.append(item.initiator.pk)
            else:
                friends_pk.append(item.target.pk)

        return Person.objects.filter(pk__in=friends_pk)

    @property
    def get_friend_requests(self):
        user = Person.objects.get(pk=self.pk)
        # Все запросы в друзья пользовалю
        all_requests = FriendRequests.objects.filter(status=0, target=user)

        # Получение pk всех друзей пользователя
        friends_pk = []
        for item in all_requests:
            if item.target == user:
                friends_pk.append(item.initiator.pk)
            else:
                friends_pk.append(item.target.pk)
        result = Person.objects.filter(pk__in=friends_pk)
        print(result == True)
        return result

    @property
    def get_gender(self):
        return GENDER_DICT.get(self.gender)

    @property
    def get_rel(self):
        return REL_DICT.get(self.relationship)
