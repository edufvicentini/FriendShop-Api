from django.db import models
from api.modules.products.model import Products
from api.modules.sells.model import Sells
from crum import get_current_user

class User_Cart_Products(models.Model):
  user = models.ForeignKey('auth.User', blank=True, null=True, default=get_current_user(), on_delete=models.CASCADE)
  product = models.ForeignKey(Products, on_delete=models.CASCADE, blank=True, null=True)
  sell = models.ForeignKey(Sells, on_delete=models.DO_NOTHING, blank=True, null=True)
  quantity = models.IntegerField()
  status = models.CharField(max_length=50, default='in cart')
  updated_at = models.DateTimeField(auto_now=True, blank=True)
  expires_in = models.DateTimeField(auto_now_add=True, blank=True)

  def save(self, *args, **kwargs):
        user = get_current_user()
        self.user = user
        super(User_Cart_Products, self).save(*args, **kwargs)