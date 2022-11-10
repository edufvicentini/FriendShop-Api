from rest_framework import generics
from api.userCartProducts.serializer import UserCartProductsSerializer
from api.userCartProducts.model import User_Cart_Products
from rest_framework.permissions import IsAuthenticated

## UserCartProducts
class UserCartProductsCreate(generics.CreateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = UserCartProductsSerializer

class UserCartProductsDelete(generics.RetrieveDestroyAPIView):
    def get_queryset(self):
        return User_Cart_Products.objects.filter(user_id=self.request.user.id)
    serializer_class = UserCartProductsSerializer

class UserCartProductsList(generics.ListAPIView):
    def get_queryset(self):
        return User_Cart_Products.objects.filter(user_id=self.request.user.id)

    serializer_class = UserCartProductsSerializer