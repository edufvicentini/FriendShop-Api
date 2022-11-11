from rest_framework import generics
from api.userCartProducts.serializer import UserCartProductsSerializer
from api.userCartProducts.model import User_Cart_Products
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from api.products.model import Products
from api.products.serializer import ProductSerializer

## UserCartProducts
class UserCartProductsCreate(generics.CreateAPIView):
    permission_classes = (IsAuthenticated,)
    def post(self, request, *args, **kwargs):
            
            # return Response(request.data)
            return self.create(request, *args, **kwargs)

    serializer_class = UserCartProductsSerializer

class UserCartProductsDelete(generics.RetrieveDestroyAPIView):
    def get_queryset(self):
        return User_Cart_Products.objects.filter(user_id=self.request.user.id)
    serializer_class = UserCartProductsSerializer

class UserCartProductsList(generics.ListAPIView):
    def get_queryset(self):
      
        return User_Cart_Products.objects.filter(user_id=self.request.user.id)
        # return User_Cart_Products.objects.raw('''select api_user_cart_products.*,
        #                                       api_products.* from api_user_cart_products
        #                                       left join api_products on api_products.id = api_user_cart_products.product_id
        #                                       where api_user_cart_products.user_id = ''' + str(self.request.user.id))

    serializer_class = UserCartProductsSerializer

# productFetch = Products.objects.get_queryset().filter(id=request.data['product'])
# productData = ProductSerializer(data=productFetch, many=True)
# productData.is_valid()
# product = {
#   "id": productData.data[0]['id'],
#   "price": productData.data[0]['id']
# }