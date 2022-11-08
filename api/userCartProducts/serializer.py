from rest_framework import serializers
from api.userCartProducts.model import User_Cart_Products
from api.products.model import Products
from django.contrib.auth.models import User

class UserCartProductsSerializer(serializers.ModelSerializer):
    user_id = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    product_id = serializers.PrimaryKeyRelatedField(queryset=Products.objects.all())

    class Meta: 
        model = User_Cart_Products
        fields = ['id', 'user_id', 'product_id', 'quantity', 'price', 'updated_at', 'expires_in']