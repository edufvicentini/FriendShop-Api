from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from api.modules.userCartProducts.serializer import UserCartProductsSerializer, UserCartSerializer, UserCartQuantitySerializer
from api.modules.userCartProducts.model import User_Cart_Products
from api.modules.products.model import Products
from api.modules.products.serializer import ProductSerializer
from api.logs.user_logs.model import User_Logs

## UserCartProducts
class UserCartProductsCreate(generics.CreateAPIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        cartQuery = User_Cart_Products.objects.filter(product_id=request.data['product'], user_id=request.user.id, status='in cart')
        cart = UserCartSerializer(cartQuery, many=True)
        
        # insert just one time
        if len(cart.data) > 0:
          return Response({ "error": "product already in the cart, use update path instead with PATCH."}, status=500)
          
        # has enough stock?
        productQuery = Products.objects.get(pk=request.data['product'])
        productData = ProductSerializer(productQuery).data

        if int(productData['stock']) < int(request.data['quantity']):
          return Response( { "error": "quantity not available for product"}, status=500)
        
        # request.data['status'] = 'in cart'
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

class UserCartUpdateProductsQuantity(generics.RetrieveUpdateAPIView):
    permission_classes = (IsAuthenticated,)
    def get_queryset(self):
        return User_Cart_Products.objects.filter(user_id=self.request.user.id, status='in cart')

    def put(self, request, *args, **kwargs):
        return Response( { "error": "not implemented. use PATCH instead" }, status=500)

    def patch(self, request, *args, **kwargs):
        cartQuery = User_Cart_Products.objects.get(pk=kwargs['pk'])
        cartRowProduct = UserCartSerializer(cartQuery).data['product']
        if int(cartRowProduct['stock']) < int(request.data['quantity']):
          return Response( { "error": "quantity not available for product"}, status=500)
        
        return self.partial_update(request, *args, **kwargs)

    
    serializer_class = UserCartQuantitySerializer



class UserCartProductsList(generics.ListAPIView):
    def get_queryset(self):
      return User_Cart_Products.objects.filter(user_id=self.request.user.id, status='in cart')
    serializer_class = UserCartSerializer
