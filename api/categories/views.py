from api.categories.model import Categories
from rest_framework import generics
from api.categories.serializer import CategorySerializer
from rest_framework.permissions import IsAdminUser
from api.admin_logs.model import Admin_Logs

class CategoryList(generics.ListAPIView):
    queryset = Categories.objects.all()
    serializer_class = CategorySerializer

class CategoryCreate(generics.CreateAPIView):
    permission_classes = (IsAdminUser,)

    def post(self, request, *args, **kwargs):
        response = self.create(request, *args, **kwargs)
        Admin_Logs.objects.create(object_type='category', object_pk=response.data['id'], action='Created')
        return response

    serializer_class = CategorySerializer

class CategoryDetail(generics.RetrieveAPIView):
    permission_classes = (IsAdminUser,)

    queryset = Categories.objects.all()
    serializer_class = CategorySerializer

class CategoryUpdate(generics.RetrieveUpdateAPIView):
    permission_classes = (IsAdminUser,)
    queryset = Categories.objects.all()

    # Overriding put method for before/after logs
    def put(self, request, *args, **kwargs):
      oldCategoryData = Categories.objects.get(pk=kwargs['pk'])
      oldCategory = CategorySerializer(oldCategoryData).data
      oldCategoryString =  f"description: {oldCategory['description']}"

      response = self.update(request, *args, **kwargs)

      if response.status_code == 200:
        newCategoryString = f"description: {response.data['description']}"
        Admin_Logs.objects.create(action='Updated. Old: { '+oldCategoryString+ ' } || New: { '+ newCategoryString + ' }', object_type='product', object_pk=kwargs['pk'])

      return response

    
    serializer_class = CategorySerializer

class CategoryDelete(generics.RetrieveDestroyAPIView):
    permission_classes = (IsAdminUser,)
    queryset = Categories.objects.all()

    def delete(self, request, *args, **kwargs):
      response = self.destroy(request, *args, **kwargs)
      
      # Admin_Logs   
      if response.status_code == 204:
        Admin_Logs.objects.create(object_type='category', object_pk=kwargs['pk'], action='Deleted')
      
      return response
    
    serializer_class = CategorySerializer