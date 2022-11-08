from django.db import models
from django.contrib.auth.models import User
from api.products.model import Products

class User_Cart_Products(models.Model):
  user_id = models.ForeignKey(User, related_name='ids', on_delete=models.CASCADE, blank=False)
  product_id = models.ForeignKey(Products, related_name='ids', on_delete=models.CASCADE, blank=False)
  quantity = models.IntegerField()
  price = models.FloatField()
  updated_at = models.DateTimeField(auto_now=True, blank=True)
  expires_in = models.DateTimeField(auto_now_add=True, blank=True)
