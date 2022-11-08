from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from api import urls as api_urls
from api.products import urls as products_urls
from api.categories import urls as categories_urls
from api.userCartProducts import urls as userCartProducts_urls
from api.auth import urls as auth_urls


urlpatterns = [
    path('admin/', admin.site.urls),
    # path('api/', include(api_urls)),
    path('api/products/', include(products_urls)),
    path('api/categories/', include(categories_urls)),
    path('api/cart/products/', include(userCartProducts_urls)),
    path('api/auth/', include(auth_urls))
]
