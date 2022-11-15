from rest_framework import serializers
from api.modules.products.model import Products
from api.modules.categories.model import Categories

class ProductSerializer(serializers.ModelSerializer):
    category = serializers.PrimaryKeyRelatedField(queryset=Categories.objects.all(), many=False) 

    class Meta:
        model = Products
        fields = ['id', 'description', 'price', 'image_url',
                  'stock', 'category', 'active', 'created_at', 'updated_at']