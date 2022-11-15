from django.db import models

class Categories(models.Model):
  description = models.CharField(max_length=200, blank=False)
  created_at = models.DateTimeField(auto_now_add=True, blank=True)
  updated_at = models.DateTimeField(auto_now=True, blank=True)
