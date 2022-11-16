from django.urls import path
from api.modules.sells.views import SellsCreate, SellsList

urlpatterns = [
    path('', SellsList.as_view(), name='list-all-sells'),  
    path('create', SellsCreate.as_view(), name='create-sell')
]