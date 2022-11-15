from rest_framework import serializers
from api.logs.user_logs.model import User_Logs

class User_LogsSerializer(serializers.ModelSerializer):
    class Meta:
        model = User_Logs
        fields = ['id', 'user_id', 'object_type', 'object_pk', 'date', 'action']