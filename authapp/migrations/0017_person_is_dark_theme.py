# Generated by Django 3.1.3 on 2020-12-28 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0016_auto_20201226_1728'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='is_dark_theme',
            field=models.BooleanField(default=False, verbose_name='Использовать темную тему'),
        ),
    ]