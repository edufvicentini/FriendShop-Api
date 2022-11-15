from rest_framework import generics
from rest_framework.permissions import IsAdminUser
from api.modules.products.model import Products
from api.modules.products.serializer import ProductSerializer
from api.logs.admin_logs.model import Admin_Logs

class ProductList(generics.ListAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductSerializer
    
class ProductCreate(generics.CreateAPIView):
  permission_classes = (IsAdminUser,)

  def post(self, request, *args, **kwargs):
      response = self.create(request, *args, **kwargs)
      Admin_Logs.objects.create(object_type='product', object_pk=response.data['id'], action='Created')
      return response

  serializer_class = ProductSerializer

class ProductDetail(generics.RetrieveAPIView):
    permission_classes = (IsAdminUser,)
    queryset = Products.objects.all()

    serializer_class = ProductSerializer

class ProductUpdate(generics.UpdateAPIView):
    permission_classes = (IsAdminUser,)
    queryset = Products.objects.all()

    # Overriding put method for before/after logs
    def put(self, request, *args, **kwargs):
      oldProductData = Products.objects.get(pk=kwargs['pk'])
      oldProduct = ProductSerializer(oldProductData).data
      oldProductString =  f"description: {oldProduct['description']}, price: {oldProduct['price']}, stock: {oldProduct['stock']}, image_url: {oldProduct['image_url']}, category: {oldProduct['category']}"

      response = self.update(request, *args, **kwargs)

      if response.status_code == 200:
        newProductString = f"description: {response.data['description']},  price: {response.data['price']}, stock: {response.data['stock']}, image_url: {response.data['image_url']}, category: {response.data['category']}"
        Admin_Logs.objects.create(action='Updated. Old: { '+oldProductString+ ' } || New: { '+ newProductString + ' }', object_type='product', object_pk=kwargs['pk'])

      return response

    serializer_class = ProductSerializer

class ProductDelete(generics.RetrieveDestroyAPIView):
    permission_classes = (IsAdminUser,)
    queryset = Products.objects.all()

    def delete(self, request, *args, **kwargs):
      response = self.destroy(request, *args, **kwargs)
      
      # Admin_Logs   
      if response.status_code == 204:
        Admin_Logs.objects.create(object_type='product', object_pk=kwargs['pk'], action='Deleted')
      
      return response

    serializer_class = ProductSerializer