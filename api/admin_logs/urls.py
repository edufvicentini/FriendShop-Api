from django.urls import path

from api.admin_logs.views import AdminLogsList

urlpatterns = [
    path('', AdminLogsList.as_view(), name='list-admin-logs')
]