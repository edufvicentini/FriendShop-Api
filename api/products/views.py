from api.products.model import Products
from rest_framework import generics
from api.products.serializer import ProductSerializer
from rest_framework.permissions import IsAdminUser, IsAuthenticated

class ProductList(generics.ListAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductSerializer

class ProductCreate(generics.CreateAPIView):
  permission_classes = (IsAdminUser,)

  queryset = Products.objects.all(),
  serializer_class = ProductSerializer

class ProductDetail(generics.RetrieveAPIView):
    permission_classes = (IsAdminUser,)

    queryset = Products.objects.all()
    serializer_class = ProductSerializer

class ProductUpdate(generics.RetrieveUpdateAPIView):
    permission_classes = (IsAdminUser,)

    queryset = Products.objects.all()
    serializer_class = ProductSerializer

class ProductDelete(generics.RetrieveDestroyAPIView):
    permission_classes = (IsAdminUser,)

    queryset = Products.objects.all()
    serializer_class = ProductSerializer