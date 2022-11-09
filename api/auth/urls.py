from django.urls import path

from api.auth.login import UserRegister, AdminLogin, UserLogin,  UserLogout
# from rest_framework.authtoken import views

urlpatterns = [
    path('register', UserRegister, name='user-register'),
    # path('login', UserLogin, name='user-login'),
    path('login', UserLogin.as_view(), name='user-login-token'),
    path('logout', UserLogout, name='user-login'),
    path('login/admin', AdminLogin, name='user-is-admin')
]