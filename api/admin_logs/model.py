from django.db import models
from api.products.model import Products

class Admin_Logs(models.Model):
  product = models.ForeignKey(Products, on_delete=models.DO_NOTHING, blank=True, null=True)
  date = models.DateTimeField(auto_now_add=True, blank=True)
  action = models.CharField(max_length=500, blank=False)