from rest_framework import serializers
from api.admin_logs.model import Admin_Logs
from api.products.model import Products

class Admin_LogsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Admin_Logs
        fields = ['id', 'object_type', 'object_pk', 'date', 'action']