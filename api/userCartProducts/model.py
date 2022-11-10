from django.db import models
from django.contrib.auth.models import User
from api.products.model import Products
from crum import get_current_user, get_current_request

class User_Cart_Products(models.Model):
  user_id = models.ForeignKey('auth.User', blank=True, null=True, default=get_current_user(), on_delete=models.CASCADE)
  product_id = models.ForeignKey(Products, related_name='ids', on_delete=models.CASCADE, blank=False)
  quantity = models.IntegerField()
  price = models.FloatField()
  updated_at = models.DateTimeField(auto_now=True, blank=True)
  expires_in = models.DateTimeField(auto_now_add=True, blank=True)

  def save(self, *args, **kwargs):
        user = get_current_user()
        self.user_id = user
        super(User_Cart_Products, self).save(*args, **kwargs)
