from django.db import models

class Sells(models.Model):
  total = models.FloatField()
  status = models.CharField(max_length=50, blank=False)
  created_at = models.DateTimeField(auto_now_add=True, blank=True)
  checkout_at = models.DateTimeField(auto_now_add=True, blank=True)