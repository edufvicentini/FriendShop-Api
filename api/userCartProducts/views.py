from rest_framework import generics
from api.userCartProducts.serializer import UserCartProductsSerializer
from api.userCartProducts.model import User_Cart_Products
from rest_framework.permissions import IsAuthenticated

from django.contrib.auth.models import User
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token

## UserCartProducts
## a única porta de entrada aqui deve ser o próprio token
# @api_view(['POST']) 
# def UserRegister(request):
#     username = request.data['username']
#     email = request.data['email']
#     password = request.data['password']
#     user = User.objects.create_user(username=username, password=password, email=email)
#     user.save()

#     return Response('user created')

class UserCartProductsCreate(generics.CreateAPIView):
    permission_classes = (IsAuthenticated,)


    queryset = User_Cart_Products.objects.all()
    serializer_class = UserCartProductsSerializer

class UserCartProductsDelete(generics.RetrieveDestroyAPIView):
    queryset = User_Cart_Products.objects.all()
    serializer_class = UserCartProductsSerializer

class UserCartProductsList(generics.ListAPIView):
    queryset = User_Cart_Products.objects.all()
    serializer_class = UserCartProductsSerializer
