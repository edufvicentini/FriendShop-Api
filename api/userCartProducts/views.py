from rest_framework import generics
from api.userCartProducts.serializer import UserCartProductsSerializer
from api.userCartProducts.model import User_Cart_Products
from rest_framework.permissions import IsAuthenticated

from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request
import logging

## UserCartProducts
## a única porta de entrada aqui deve ser o próprio token
@api_view(['POST']) 
def Test(request):
    current_user = request.user
    
    return Response(current_user.id)

class UserCartProductsCreate(generics.CreateAPIView):
    permission_classes = (IsAuthenticated,)

    # queryset = User_Cart_Products.objects.all()
    def post_queryset(self):
        return User_Cart_Products.objects.values(user_id=self.request.user.id)
    serializer_class = UserCartProductsSerializer

class UserCartProductsDelete(generics.RetrieveDestroyAPIView):
    queryset = User_Cart_Products.objects.all()
    serializer_class = UserCartProductsSerializer

class UserCartProductsList(generics.ListAPIView):
    def get_queryset(self):
        return User_Cart_Products.objects.filter(user_id=self.request.user.id)

    serializer_class = UserCartProductsSerializer

    
# @api_view(['GET']) 
# def GetUserCart(request):
#     current_user = request.user
#     queryset = User_Cart_Products.objects.filter(user_id=current_user.id)
#     serializer_class = UserCartProductsSerializer
    # if serializer_class.is_valid():
    # return Response(queryset)