from rest_framework import generics
from rest_framework.permissions import IsAdminUser
from api.logs.admin_logs.model import Admin_Logs
from api.logs.admin_logs.serializer import Admin_LogsSerializer

class AdminLogsList(generics.ListAPIView):
    permission_classes = (IsAdminUser,)

    queryset = Admin_Logs.objects.all()
    serializer_class = Admin_LogsSerializer