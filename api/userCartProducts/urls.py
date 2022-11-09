from django.urls import path

#UserCartProducts
from api.userCartProducts.views import UserCartProductsCreate, UserCartProductsList, UserCartProductsDelete, Test

urlpatterns = [
    #UserCartProducts
    path('', UserCartProductsList.as_view(), name='list-products-in-cart'),  
    # path('test', Test, name='list-products-in-cart'),
    path('add', UserCartProductsCreate.as_view(), name='add-product-to-cart'),  
    path('delete', UserCartProductsDelete.as_view(), name='remove-product-from-cart'),
  
]