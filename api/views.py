from django.shortcuts import render
from .models import Products
from rest_framework import generics
from .serializers import ProductSerializer, UserCartProductsSerializer

### Products
class ProductCreate(generics.CreateAPIView):
    queryset = Products.objects.all(),
    serializer_class = ProductSerializer

class ProductList(generics.ListAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductSerializer

class ProductDetail(generics.RetrieveAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductSerializer

class ProductUpdate(generics.RetrieveUpdateAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductSerializer

class ProductDelete(generics.RetrieveDestroyAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductSerializer


### UserCartProducts
class UserCartProductsCreate(generics.CreateAPIView):
    queryset = Products.objects.all(),
    serializer_class = UserCartProductsSerializer

class UserCartProductsDelete(generics.RetrieveDestroyAPIView):
    queryset = Products.objects.all()
    serializer_class = UserCartProductsSerializer

class UserCartProductsList(generics.ListAPIView):
    queryset = Products.objects.all()
    serializer_class = UserCartProductsSerializer
