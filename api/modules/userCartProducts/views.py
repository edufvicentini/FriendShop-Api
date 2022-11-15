from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from api.modules.userCartProducts.serializer import UserCartProductsSerializer, UserCartSerializer
from api.modules.userCartProducts.model import User_Cart_Products
from api.logs.user_logs.model import User_Logs

## UserCartProducts
class UserCartProductsCreate(generics.CreateAPIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        response = self.create(request, *args, **kwargs)
        User_Logs.objects.create(user_id=request.user.id ,object_type='product', object_pk=response.data['product'], action='Added to Cart')
        return response

    serializer_class = UserCartProductsSerializer

class UserCartProductsDelete(generics.RetrieveDestroyAPIView):
    def get_queryset(self):
        return User_Cart_Products.objects.filter(user_id=self.request.user.id)

    def delete(self, request, *args, **kwargs):
      response = self.destroy(request, *args, **kwargs)
      
      # Admin_Logs   
      if response.status_code == 204:
        User_Logs.objects.create(user_id=request.user.id, object_type='product', object_pk=kwargs['pk'], action='Removed from Cart')
      
      return response    
    serializer_class = UserCartProductsSerializer

class UserCartProductsList(generics.ListAPIView):
    def get_queryset(self):
      return User_Cart_Products.objects.filter(user_id=self.request.user.id)
    serializer_class = UserCartSerializer
