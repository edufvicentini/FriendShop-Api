from rest_framework import generics
from rest_framework.permissions import IsAdminUser
from api.logs.user_logs.model import User_Logs
from api.logs.user_logs.serializer import User_LogsSerializer

class UserLogsList(generics.ListAPIView):
    permission_classes = (IsAdminUser,)

    queryset = User_Logs.objects.all()
    serializer_class = User_LogsSerializer