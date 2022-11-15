from rest_framework import serializers
from api.admin_logs.model import Admin_Logs
from api.products.model import Products

class Admin_LogsSerializer(serializers.ModelSerializer):
    product = serializers.PrimaryKeyRelatedField(queryset=Products.objects.all(), many=False) 
 
    class Meta:
        model = Admin_Logs
        fields = ['id', 'product', 'date', 'action']