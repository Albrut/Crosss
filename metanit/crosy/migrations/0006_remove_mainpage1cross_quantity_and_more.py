# Generated by Django 4.1.3 on 2022-11-22 15:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crosy', '0005_mainpage1cross_delete_tvshow'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mainpage1cross',
            name='quantity',
        ),
        migrations.RemoveField(
            model_name='mainpage1cross',
            name='trailers_film',
        ),
    ]
