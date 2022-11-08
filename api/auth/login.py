from django.contrib.auth.models import User
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser
from rest_framework.decorators import api_view, permission_classes

from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

class CustomObtainAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        response = super(CustomObtainAuthToken, self).post(request, *args, **kwargs)
        token = Token.objects.get(key=response.data['token'])
        return Response({'token': token.key, 'id': token.user_id})

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