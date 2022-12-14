from django.db import models
from api.modules.categories.model import Categories

class Products(models.Model):
  description = models.CharField(max_length=200, blank=False)
  price = models.FloatField()
  image_url = models.CharField(max_length=254)
  stock = models.IntegerField()
  category = models.ForeignKey(Categories, on_delete=models.DO_NOTHING, blank=True, null=True)
  active = models.BooleanField()
  created_at = models.DateTimeField(auto_now_add=True, blank=True)
  updated_at = models.DateTimeField(auto_now=True, blank=True)
