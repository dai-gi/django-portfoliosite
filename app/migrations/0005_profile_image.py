# Generated by Django 2.2.19 on 2021-02-28 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20210228_1814'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='profile', verbose_name='イメージ画像'),
        ),
    ]
