from django.urls import path

# Products
from .views import ProductList, ProductCreate, ProductDetail, ProductDelete, ProductUpdate

#UserCartProducts
from .views import UserCartProductsCreate, UserCartProductsList, UserCartProductsDelete

urlpatterns = [
    #Products
    path('products/', ProductList.as_view(), name='list-products'),  
    path('products/create/', ProductCreate.as_view(), name='create-customer'),
    path('products/<int:pk>', ProductDetail.as_view(), name='detail-product'),
    path('products/update/<int:pk>', ProductUpdate.as_view(), name='update-product'),
    path('products/delete/<int:pk>', ProductDelete.as_view(), name='delete-product'),

    #UserCartProducts
    path('user-cart-products/<int:user_id>', UserCartProductsList.as_view(), name='list-products-in-cart'),  
    path('user-cart-products/<int:user_id>/add/', UserCartProductsCreate.as_view(), name='add-product-to-cart'),  
    path('user-cart-products/<int:user_id>/delete/<int:pk>', UserCartProductsDelete.as_view(), name='remove-product-from-cart')
    

]