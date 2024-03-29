# Generated by Django 3.1.3 on 2021-11-29 02:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsapp', '0011_auto_20211128_2344'),
    ]

    operations = [
        migrations.AddField(
            model_name='newsitem',
            name='is_community',
            field=models.BooleanField(default=False, verbose_name='Новость сообщества'),
        ),
        migrations.AlterField(
            model_name='newsitem',
            name='image',
            field=models.FileField(blank=True, default=None, null=True, upload_to='news_images', verbose_name='Изображние'),
        ),
    ]
