# Generated by Django 4.1.3 on 2022-11-27 10:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crosy', '0017_mainpage1_cross_titlq1_1_mainpage1_cross_titlq2_1_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mainpage1_cross',
            name='titlq1_1',
        ),
        migrations.RemoveField(
            model_name='mainpage1_cross',
            name='titlq2_1',
        ),
        migrations.RemoveField(
            model_name='mainpage1_cross',
            name='titlq2_2',
        ),
    ]