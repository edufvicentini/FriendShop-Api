from rest_framework import serializers
from api.userCartProducts.model import User_Cart_Products
from api.products.serializer import ProductSerializer
from api.products.model import Products
from rest_framework.response import Response

class ProductInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = ['id', 'price']
    
    

            # id =  serializers.SlugRelatedField(queryset=Products.objects.all(), many=False, slug_field='id')
    # price = serializers.SlugRelatedField(queryset=Products.objects.all(), many=False, slug_field='price')

    # def to_representation(self, value):
    #     productFetch = Products.objects.get_queryset().filter(id=value[0])
    #     productData = ProductSerializer(data=productFetch, many=True)
    #     productData.is_valid()
    #     product = {
    #       "id": productData.data[0]['id'],
    #       "price": productData.data[0]['id']
    #     }
    #     return product
    
    

class UserCartProductsSerializer(serializers.ModelSerializer):
    product = serializers.PrimaryKeyRelatedField(queryset=Products.objects.all(), many=False) 

    class Meta: 
        model = User_Cart_Products
        fields = ['id', 'user_id', 'product','quantity', 'updated_at', 'expires_in']
        depth = 2

class UserCartSerializer(serializers.ModelSerializer):
    class Meta: 
        model = User_Cart_Products
        fields = ['id', 'user_id', 'product','quantity', 'updated_at', 'expires_in']
        depth = 2