# Generated by Django 2.2 on 2020-11-13 12:55

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('messengerapp', '0002_auto_20201113_0840'),
    ]

    operations = [
        migrations.AddField(
            model_name='chat',
            name='title',
            field=models.CharField(default=django.utils.timezone.now, max_length=50, verbose_name='Название'),
            preserve_default=False,
        ),
    ]