from django.db import models
from api.products.model import Products

class Admin_Logs(models.Model):
  object_type = models.CharField(max_length=50, blank=False)
  object_pk = models.IntegerField()
  date = models.DateTimeField(auto_now_add=True, blank=True)
  action = models.CharField(max_length=500, blank=False)