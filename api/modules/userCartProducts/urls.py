from django.urls import path
from api.modules.userCartProducts.views import UserCartProductsCreate, UserCartProductsList, UserCartProductsDelete, UserCartUpdateProductsQuantity

urlpatterns = [
    path('', UserCartProductsList.as_view(), name='list-products-in-cart'),  
    path('add', UserCartProductsCreate.as_view(), name='add-product-to-cart'),  
    path('delete/<int:pk>', UserCartProductsDelete.as_view(), name='remove-product-from-cart'),
    path('update/<int:pk>', UserCartUpdateProductsQuantity.as_view(), name='update-product-quantity'),
  
]