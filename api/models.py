from django.db import models

class Sells(models.Model):
  value = models.FloatField()
  discount = models.FloatField()
  total = models.FloatField()
  status = models.CharField(max_length=200, blank=False)
  created_at = models.DateTimeField(auto_now_add=True, blank=True)