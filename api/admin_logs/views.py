# from api.products.model import Products
from rest_framework import generics
from api.admin_logs.model import Admin_Logs
from api.admin_logs.serializer import Admin_LogsSerializer
from rest_framework.permissions import IsAdminUser

class AdminLogsList(generics.ListAPIView):
    permission_classes = (IsAdminUser,)

    queryset = Admin_Logs.objects.all()
    serializer_class = Admin_LogsSerializer