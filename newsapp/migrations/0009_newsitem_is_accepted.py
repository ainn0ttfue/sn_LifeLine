# Generated by Django 3.1.3 on 2021-11-19 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsapp', '0008_newsitem_is_moderated'),
    ]

    operations = [
        migrations.AddField(
            model_name='newsitem',
            name='is_accepted',
            field=models.BooleanField(default=False, verbose_name='Публикация принята'),
        ),
    ]