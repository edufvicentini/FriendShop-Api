from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser
from rest_framework.decorators import api_view, permission_classes
from django.contrib.auth import logout

from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

class CustomObtainAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        response = super(CustomObtainAuthToken, self).post(request, *args, **kwargs)
        token = Token.objects.get(key=response.data['token'])
        return Response({'token': token.key, 'id': token.user_id})

@api_view(['POST']) 
def UserLogin(request):
    username = request.data['username']
    password = request.data['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return Response('Logged in Successfully')
    else:
        return Response('Wrong username or password')

@api_view(['POST']) 
def UserLogout(request):
    logout(request)

@api_view(['POST']) 
def UserRegister(request):
    username = request.data['username']
    email = request.data['email']
    password = request.data['password']
    user = User.objects.create_user(username=username, password=password, email=email)
    user.save()

    return Response('user created')

@api_view(['GET'])
@permission_classes([IsAdminUser])
def AdminLogin(request):
    # Token.objects.get(request.headers['Authorization'])
    # User.pk()
    
    return Response(request.headers['Authorization'][6:])