from dataclasses import fields
from rest_framework import serializers
from . import models



        
  
  

class ColorSerialiser(serializers.ModelSerializer):
    class Meta:
        model = models.Color
        fields = ("name" ,"id" )
        
class SizeSerialiser(serializers.ModelSerializer):
    class Meta:
        model = models.Size
        fields =( "name", "id" )
        
class ShopSerialiser(serializers.ModelSerializer):
    class Meta:
        model = models.Shop
        fields =( "__all__" )


class ProductListSerializer(serializers.ModelSerializer):
    size = serializers.SlugRelatedField(
        many=True,
        slug_field='name',
        # queryset=models.Color.objects.all())
        read_only=True,
        
     )
    
    color = serializers.SlugRelatedField(
        many=True,
        # queryset=models.Color.objects.all()
        
        read_only=True,
        slug_field='name'
     )
    
   
    class Meta:
        model = models.Product
        fields = "id" , "shope", "name" , "image" , "price" , "color" , "size" ,"category", "type" , "amount"
    
    def to_representation(self, instance):
        
        # self.fields['product_detail'] =  ProductDetailSerialiser(read_only=True)
        self.fields['shope'] =  ShopSerialiser(read_only=True , )
        # self.fields['color'] =  ColorSerialiser(read_only=True, many=True)
        
        return super(ProductListSerializer, self).to_representation(instance)
       
      
      
