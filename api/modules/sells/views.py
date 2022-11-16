from rest_framework import generics
from rest_framework.permissions import IsAdminUser
from api.modules.sells.model import Sells
from api.modules.sells.serializer import SellsSerializer
from api.modules.userCartProducts.model import User_Cart_Products
from api.modules.userCartProducts.serializer import UserCartSerializer
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

    def post(self, request, *args, **kwargs):
        cartQuery = User_Cart_Products.objects.filter(user_id=self.request.user.id)
        cart = UserCartSerializer(cartQuery, many=True)
        request.data['total'] = self.calculate_total(cart.data)
        response = self.create(request, *args, **kwargs)
        User_Logs.objects.create(object_type='sell', object_pk=response.data['id'], action='Created')
        return response

    serializer_class = SellsSerializer