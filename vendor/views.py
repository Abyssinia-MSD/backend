from itertools import product
from math import prod
from django.shortcuts import render
from rest_framework import serializers, viewsets
from django.contrib.auth.decorators import login_required
from . import seriliazer
from . import models
from . import form
from django.contrib import messages
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.permissions import AllowAny
from rest_framework import generics, status, permissions
from django.http import JsonResponse
from .permisions import IsAdminOrReadOnly
from rest_framework.permissions import IsAuthenticated 


# Create your views here.

class ProductListView(viewsets.ModelViewSet):
    
    queryset = models.Product.objects.all()
    serializer_class = seriliazer.ProductListSerializer
    permission_classes = (IsAdminOrReadOnly,)
   
