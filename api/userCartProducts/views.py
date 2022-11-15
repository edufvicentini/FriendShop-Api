from rest_framework import generics
from api.userCartProducts.serializer import UserCartProductsSerializer, UserCartSerializer
from api.userCartProducts.model import User_Cart_Products
from rest_framework.permissions import IsAuthenticated

## UserCartProducts
class UserCartProductsCreate(generics.CreateAPIView):
    permission_classes = (IsAuthenticated,)
    def post(self, request, *args, **kwargs):
      
      return self.create(request, *args, **kwargs)

    serializer_class = UserCartProductsSerializer

class UserCartProductsDelete(generics.RetrieveDestroyAPIView):
    def get_queryset(self):
        return User_Cart_Products.objects.filter(user_id=self.request.user.id)
    serializer_class = UserCartProductsSerializer

class UserCartProductsList(generics.ListAPIView):
    def get_queryset(self):
      return User_Cart_Products.objects.filter(user_id=self.request.user.id)
    serializer_class = UserCartSerializer
