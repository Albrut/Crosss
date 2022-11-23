# Generated by Django 4.1.3 on 2022-11-22 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crosy', '0004_tvshow_delete_mainpage1cross'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mainpage1cross',
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
            name='TVShow',
        ),
    ]