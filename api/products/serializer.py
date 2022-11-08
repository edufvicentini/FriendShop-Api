from rest_framework import serializers
from api.products.model import Products

class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Products
        fields = ['id', 'description', 'price', 'image_url',
                  'stock', 'category_id', 'active', 'created_at', 'updated_at']