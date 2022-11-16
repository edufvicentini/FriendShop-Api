from rest_framework import serializers
from api.modules.sells.model import Sells

class SellsSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Sells
        fields = ['id', 'total', 'status', 'checkout_at', 'created_at']