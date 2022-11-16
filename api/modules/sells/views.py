from rest_framework import generics
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from api.modules.sells.model import Sells
from api.modules.sells.serializer import SellsSerializer
from api.modules.userCartProducts.model import User_Cart_Products
from api.modules.userCartProducts.serializer import UserCartSerializer
from api.modules.products.model import Products
from api.modules.products.serializer import ProductSerializer
from api.logs.user_logs.model import User_Logs

class SellsList(generics.ListAPIView):
    permission_classes = (IsAdminUser,)
    
    queryset = Sells.objects.all()
    serializer_class = SellsSerializer

class SellsCreate(generics.CreateAPIView):
    permission_classes = (IsAdminUser,)

    def calculate_total(*args):
        cartSerializer = args[1]
        total = 0
        for row in cartSerializer:
          productData = row['product']
          print(row['quantity'], productData['price'] )
          total += row['quantity']*productData['price']
        return total

    def is_product_in_cart_out_of_stock(*args):
      cartSerializer = args[1]
      for row in cartSerializer:
        productData = row['product']
        if row['quantity'] > productData['stock']:
          return { 'product': productData['description'], 'is_out_of_stock':True}
      return {'is_out_of_stock':False}

    def set_items_status_sold(*args):
      cartSerializer = args[1]
      response = args[2]
      for row in cartSerializer:
        cart_item = User_Cart_Products.objects.get(pk=row['id'])
        cart_item.status = 'sold'
        cart_item.sell_id = response.data['id']
        cart_item.save()

    def subtract_quantity_from_stock(*args):
      cartSerializer = args[1]
      for row in cartSerializer:
        productData = row['product']
        product = Products.objects.get(pk=productData['id'])
        product.stock -= int(row['quantity'])
        product.save()

    def post(self, request, *args, **kwargs):
        cartQuery = User_Cart_Products.objects.filter(user_id=self.request.user.id, status='in cart')
        cart = UserCartSerializer(cartQuery, many=True)

        if len(cart.data) == 0:
          return Response({ "error": "no products in cart" }, status=500)

        # test if product is out of stock
        some_product_out_of_stock = self.is_product_in_cart_out_of_stock(cart.data)
        if some_product_out_of_stock['is_out_of_stock']:
          return Response({ "error": f"product {some_product_out_of_stock['product']} out of stock" }, status=500)

        request.data['total'] = self.calculate_total(cart.data)

        response = self.create(request, *args, **kwargs)
        
        if response.status_code == 201:
          print('venda feita com sucesso')
          self.set_items_status_sold(cart.data, response)
          self.subtract_quantity_from_stock(cart.data)
          User_Logs.objects.create(user_id=request.user.id,object_type='sell', object_pk=response.data['id'], action='Created') 
          return response
        else:
          return Response({"erro": "some error occurred during sell creation"}, status=500)

    serializer_class = SellsSerializer