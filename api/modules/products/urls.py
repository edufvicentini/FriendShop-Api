from django.urls import path

from api.modules.products.views import ProductList, ProductCreate, ProductDetail, ProductDelete, ProductUpdate

urlpatterns = [
    path('', ProductList.as_view(), name='list-products'),  
    path('create/', ProductCreate.as_view(), name='create-customer'),
    path('<int:pk>', ProductDetail.as_view(), name='detail-product'),
    path('update/<int:pk>', ProductUpdate.as_view(), name='update-product'),
    path('delete/<int:pk>', ProductDelete.as_view(), name='delete-product')
]