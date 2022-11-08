from django.urls import path

# Products
from api.categories.views import CategoryList, CategoryCreate, CategoryDetail, CategoryUpdate, CategoryDelete

urlpatterns = [
    #Products
    path('', CategoryList.as_view(), name='list-categories'),  
    path('create/', CategoryCreate.as_view(), name='create-category'),
    path('<int:pk>', CategoryDetail.as_view(), name='detail-category'),
    path('update/<int:pk>', CategoryUpdate.as_view(), name='update-category'),
    path('delete/<int:pk>', CategoryDelete.as_view(), name='delete-category')
]