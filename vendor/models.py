from ast import Or
from email.mime import image
from itertools import product
from pyexpat import model
from tkinter import CASCADE
from turtle import color
from unicodedata import category
from django.core.exceptions import ValidationError
from django.db import models
from django.conf import settings
from django_enumfield import enum

from shop import settings


class Shop(models.Model):
    name = models.CharField(max_length=200)
    logo = models.CharField(max_length=200)
    location = models.CharField(max_length=200, default=False)
    shopOwner = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="User",
                                  default=False, on_delete=models.CASCADE, null=True)

    def clean(self):
        if self.shopOwner.shop_owner != True:
            raise ValidationError('can not add customers')
        return super().clean()
    
    def __str__(self):
        return self.name


class Color(models.Model):
    name = models.CharField(max_length=50)
   
    
    def __str__(self):
        return self.name


class Size(models.Model):
   name = models.CharField(max_length=50)
    
    
   def __str__(self):
        return self.name


class Category(enum.Enum):
    WOMENS = 1
    MENS = 2
    KIDS = 3



class Type(enum.Enum):
    Afar_Traditional_Cloth = 1
    Harar_Traditional_Cloth = 2
    Gojam_Traditional_Cloth = 3
    Gonder_Traditional_Cloth = 4
    Agew_Traditional_Cloth = 5
    Arsi_Traditional_Cloth = 6
    Shewa_Traditional_Cloth = 7
    Debub_Traditional_Cloth = 8
    Hadari_Traditional_Cloth = 9

  


class Product(models.Model):
    shope = models.ForeignKey(Shop , on_delete=models.CASCADE , null=False , default=False )
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to="images/", null=True)
    price = models.PositiveIntegerField()
    amount = models.PositiveIntegerField(null=True)
    size = models.ManyToManyField(Size)
    color = models.ManyToManyField(Color)
    category = enum.EnumField(Category, default=Category.WOMENS)
    type =enum.EnumField(Type, default=Type.Afar_Traditional_Cloth)
    
    
    def __str__(self):
        return self.name



