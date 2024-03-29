# Generated by Django 3.1.3 on 2021-11-29 11:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('communityapp', '0002_communitynewsitem'),
    ]

    operations = [
        migrations.CreateModel(
            name='CommunityParticipant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.IntegerField(choices=[(0, 'Подписчик'), (1, 'Публикатор')], default=0, verbose_name='Роль в сообществе')),
                ('community', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='communityapp.community', verbose_name='Сообщество')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Участник')),
            ],
            options={
                'verbose_name': 'Участник сообщества',
                'verbose_name_plural': 'Участники сообщества',
            },
        ),
    ]
