# Generated by Django 4.1.3 on 2022-11-22 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crosy', '0003_rename_main_page_1_cross_mainpage1cross'),
    ]

    operations = [
        migrations.CreateModel(
            name='TVShow',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='')),
                ('quantity', models.IntegerField()),
                ('trailers_film', models.URLField(null=True)),
                ('created_date', models.DateField(auto_now_add=True)),
                ('updated_date', models.DateField(auto_now=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Mainpage1cross',
        ),
    ]