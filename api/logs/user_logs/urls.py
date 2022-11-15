from django.urls import path
from api.logs.user_logs.views import UserLogsList

urlpatterns = [
    path('', UserLogsList.as_view(), name='list-user-logs')
]