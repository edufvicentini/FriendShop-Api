from rest_framework import serializers
from api.modules.userCartProducts.model import User_Cart_Products
from api.modules.products.model import Products

class ProductInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = ['id', 'price']

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