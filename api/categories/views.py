from api.categories.model import Categories
from rest_framework import generics
from api.categories.serializer import CategorySerializer
from rest_framework.permissions import IsAdminUser

### Categories
class CategoryList(generics.ListAPIView):
    queryset = Categories.objects.all()
    serializer_class = CategorySerializer

class CategoryCreate(generics.CreateAPIView):
  permission_classes = (IsAdminUser,)

  queryset = Categories.objects.all(),
  serializer_class = CategorySerializer

class CategoryDetail(generics.RetrieveAPIView):
    permission_classes = (IsAdminUser,)

    queryset = Categories.objects.all()
    serializer_class = CategorySerializer

class CategoryUpdate(generics.RetrieveUpdateAPIView):
    permission_classes = (IsAdminUser,)

    queryset = Categories.objects.all()
    serializer_class = CategorySerializer

class CategoryDelete(generics.RetrieveDestroyAPIView):
    permission_classes = (IsAdminUser,)

    queryset = Categories.objects.all()
    serializer_class = CategorySerializer