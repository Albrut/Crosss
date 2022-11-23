from django.db import models


class Mainpage1_cross(models.Model):
    image1 = models.ImageField(upload_to='')
    image2 = models.ImageField(upload_to='')
    image3 = models.ImageField(upload_to='')
    text1_1 = models.CharField(max_length=50, null=True)
    text1_2 = models.CharField(max_length=50, null=True)
    text1_3 = models.CharField(max_length=50, null=True)
    text2_1 = models.CharField(max_length=50, null=True)
    text2_2 = models.CharField(max_length=50, null=True)
    text2_3 = models.CharField(max_length=50, null=True)
    text3_1 = models.CharField(max_length=50, null=True)
    text3_2 = models.CharField(max_length=50, null=True)
    text3_3 = models.CharField(max_length=50, null=True)

class About_us(models.Model):
    image1 = models.ImageField(upload_to='')
    image2 = models.ImageField(upload_to='')
    image3 = models.ImageField(upload_to='')
    text1_1 = models.CharField(max_length=50,null=True)
    text1_2 = models.CharField(max_length=50,null=True)
    text1_3 = models.CharField(max_length=50,null=True)
    text2_1 = models.CharField(max_length=50,null=True)
    text2_2 = models.CharField(max_length=50,null=True)
    text2_3 = models.CharField(max_length=50,null=True)
    text3_1 = models.CharField(max_length=50,null=True)
    text3_2 = models.CharField(max_length=50,null=True)
    text3_3 = models.CharField(max_length=50,null=True)




class Contact(models.Model):
    name1 = models.CharField(max_length=50, null=True)
    name2 = models.CharField(max_length=50, null=True)
    name3 = models.CharField(max_length=50, null=True)
    insta = models.CharField(max_length=40, null=True)
    phone_number1 = models.CharField(max_length=15)
    phone_number2 = models.CharField(max_length=15)
    phone_number3 = models.CharField(max_length=15)
    adres = models.CharField(max_length=100)
    image_mem = models.ImageField(upload_to='')
    email = models.EmailField()
    image_down1 = models.ImageField(upload_to='')
    image_down2 = models.ImageField(upload_to='')
    image_down3 = models.ImageField(upload_to='')


class Products(models.Model):
    image1 = models.ImageField(upload_to='')
    image2 = models.ImageField(upload_to='')
    image3 = models.ImageField(upload_to='')
    text1_1 = models.TextField()
    text1_2 = models.TextField()
    text2_1 = models.TextField()
    text2_2 = models.TextField()
    image_down1 = models.ImageField(upload_to='')
    image_down2 = models.ImageField(upload_to='')
    image_down3 = models.ImageField(upload_to='')