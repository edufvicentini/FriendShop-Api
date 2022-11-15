from django.db import models

class User_Logs(models.Model):
  user_id = models.IntegerField()
  object_type = models.CharField(max_length=50, blank=False)
  object_pk = models.IntegerField()
  date = models.DateTimeField(auto_now_add=True, blank=True)
  action = models.CharField(max_length=500, blank=False)