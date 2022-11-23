from django.forms import forms
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from . import models, forms



def cross_main_p(request):
    cross_1 = models.Mainpage1_cross.objects.all()
    return render(request, 'index.html', {'cross_1' : cross_1})

def about(request):
    about = models.About_us.objects.all()
    return render(request, 'about.html', {'about':about})

def contact(request):
    contact = models.Contact.objects.all()
    return render(request, 'contact.html', {'contact': contact})
def product(request):
    products = models.Products.objects.all()
    return render(request, 'products.html', {'contact': products})








