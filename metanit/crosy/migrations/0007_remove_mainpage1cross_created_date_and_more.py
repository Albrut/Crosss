# Generated by Django 4.1.3 on 2022-11-22 15:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crosy', '0006_remove_mainpage1cross_quantity_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mainpage1cross',
            name='created_date',
        ),
        migrations.RemoveField(
            model_name='mainpage1cross',
            name='updated_date',
        ),
    ]
