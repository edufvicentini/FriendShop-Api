from django.db import models

class Sells(models.Model):
  value = models.FloatField()
  discount = models.FloatField()
  total = models.FloatField()
  status = models.CharField(max_length=200, blank=False)
  created_at = models.DateTimeField(auto_now_add=True, blank=True)

class User_Logs(models.Model):
  action = models.CharField(max_length=500, blank=False)
  product_id = models.IntegerField()
  date = models.DateTimeField(auto_now_add=True, blank=True)

class Admin_Logs(models.Model):
  action = models.CharField(max_length=500, blank=False)
  product_id = models.IntegerField()
  date = models.DateTimeField(auto_now_add=True, blank=True)
