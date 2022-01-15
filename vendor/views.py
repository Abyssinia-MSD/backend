from django.shortcuts import render
from rest_framework import serializers, viewsets
from django.contrib.auth.decorators import login_required
from . import seriliazer
from . import models
from . import form
from django.contrib import messages
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST


# Create your views here.

class ProductListView(viewsets.ModelViewSet):
    serializer_class = seriliazer.ProductListSerializer
    queryset = models.Product.objects.all()

    def get_queryset(self):
        return super().get_queryset()
    

@login_required(login_url='/login')
def index(request):
    # t_list = Task.objects.order_by('date_created')
    # tasks_list = tasks_list.filter(author=request.user)
    if request.method == "POST":
        data = request.POST
        product_form = form.ProductForm(data)
        if product_form.is_valid():
            product = product_form.save()
            # task.author=request.user
            product.save()
            messages.success(request, 'Product Item created!')
      
    return Response(status=HTTP_200_OK)
