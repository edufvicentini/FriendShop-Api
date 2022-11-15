from rest_framework import serializers
from api.modules.categories.model import Categories

class CategorySerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Categories
        fields = ['id', 'description', 'created_at', 'updated_at']