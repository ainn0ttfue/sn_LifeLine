# Generated by Django 3.1.3 on 2022-06-08 05:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0018_auto_20211118_2210'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='gender',
            field=models.CharField(blank=True, choices=[['male', 'Мужской'], ['female', 'Женский']], default=None, max_length=10, verbose_name='Пол'),
        ),
    ]
