# Generated by Django 2.2.19 on 2021-02-28 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='career',
            field=models.TextField(default=1, max_length=500, verbose_name='経歴'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='programming_language',
            field=models.TextField(default=1, max_length=500, verbose_name='プログラミング言語'),
            preserve_default=False,
        ),
    ]