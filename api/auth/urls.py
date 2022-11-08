from django.urls import path

from api.auth.login import UserRegister, AdminLogin, CustomObtainAuthToken
# from rest_framework.authtoken import views

urlpatterns = [
    path('register', UserRegister, name='user-register'),
    path('login', CustomObtainAuthToken.as_view()),
    path('login/admin', AdminLogin, name='user-is-admin')
]