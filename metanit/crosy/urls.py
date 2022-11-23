from django.urls import path
from . import views

urlpatterns = [
    path('order/', views.cross_main_p, name='cross_1'),
    path('about/', views.about, name='about'),
    path('home/',views.cross_main_p,name='index')
]