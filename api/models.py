from django.db import models

class Products(models.Model):
  description = models.CharField(max_length=200, blank=False)
  price = models.FloatField()
  image_url = models.CharField(max_length=255)
  stock = models.IntegerField()
  category_id = models.IntegerField()
  active = models.BooleanField()
  created_at = models.DateTimeField(auto_now_add=True, blank=True)
  updated_at = models.DateTimeField(auto_now_add=True, blank=True)

class Users(models.Model):
  email = models.CharField(max_length=200, blank=False)
  password = models.CharField(max_length=32, blank=False)
  is_admin = models.BooleanField(default=False)
  created_at = models.DateTimeField(auto_now_add=True, blank=True)
  updated_at = models.DateTimeField(auto_now_add=True, blank=True)

class User_Cart_Products(models.Model):
  user_id = models.IntegerField()
  product_id = models.IntegerField()
  quantity = models.IntegerField()
  price = models.FloatField()
  updated_at = models.DateTimeField(auto_now_add=True, blank=True)
  expires_in = models.DateTimeField(auto_now_add=True, blank=True)

class Categories(models.Model):
  description = models.CharField(max_length=200, blank=False)
  active = models.BooleanField()
  created_at = models.DateTimeField(auto_now_add=True, blank=True)
  updated_at = models.DateTimeField(auto_now_add=True, blank=True)

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

  