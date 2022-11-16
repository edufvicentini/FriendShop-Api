from django.contrib import admin
from django.urls import path
from django.conf.urls import include

# User
from api.auth import urls as auth_urls

# Modules
from api.modules.products import urls as products_urls
from api.modules.categories import urls as categories_urls
from api.modules.userCartProducts import urls as userCartProducts_urls
from api.modules.sells import urls as sells_urls

#Logs
from api.logs.admin_logs import urls as admin_logs_urls
from api.logs.user_logs import urls as user_logs_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/products/', include(products_urls)),
    path('api/categories/', include(categories_urls)),
    path('api/cart/products/', include(userCartProducts_urls)),
    path('api/auth/', include(auth_urls)),
    path('api/admin/logs', include(admin_logs_urls)),
    path('api/user/logs', include(user_logs_urls)),
    path('api/sells/', include(sells_urls))    
]