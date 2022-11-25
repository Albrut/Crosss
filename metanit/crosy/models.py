from django.db import models


class Mainpage1_cross(models.Model):
    imga1 = models.ImageField(upload_to='',default='default.jpg')
    imga2= models.ImageField(upload_to='',default='default.jpg')
    imga3 = models.ImageField(upload_to='',default='default.jpg')
    txta = models.CharField(max_length=50,null=True)
    txta2 = models.CharField(max_length=50,null=True)
    txta3 = models.CharField(max_length=50,null=True)
    txta4 = models.CharField(max_length=50,null=True)
    txta5= models.CharField(max_length=50,null=True)
    txta6 = models.CharField(max_length=50,null=True)
    prc1 = models.CharField(max_length=10,null=True)
    prc2 = models.CharField(max_length=10, null=True)
    prc3 = models.CharField(max_length=10, null=True)

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
    imge1 = models.ImageField(upload_to='', default='default.jpg')
    imge2 = models.ImageField(upload_to='', default='default.jpg')
    imge3 = models.ImageField(upload_to='', default='default.jpg')
    txte1 = models.CharField(max_length=50, null=True)
    txte2 = models.CharField(max_length=50, null=True)
    txte3 = models.CharField(max_length=50, null=True)
    txte4 = models.CharField(max_length=50, null=True)
    txte5 = models.CharField(max_length=50, null=True)
    txte6 = models.CharField(max_length=50, null=True)