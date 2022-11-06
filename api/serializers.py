from rest_framework import serializers
from .models import Products, User_Cart_Products

class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Products
        fields = ['id', 'description', 'price', 'image_url',
                  'stock', 'category_id', 'active', 'created_at', 'updated_at']

class UserCartProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = User_Cart_Products
        fields = ['id','user_id', 'product_id', 'quantity', 'price', 'updated_at', 'expires_in']
