# Generated by Django 2.2.19 on 2021-02-28 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20210228_1755'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='career',
            field=models.TextField(verbose_name='経歴'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='programming_language',
            field=models.TextField(verbose_name='プログラミング言語'),
        ),
    ]
