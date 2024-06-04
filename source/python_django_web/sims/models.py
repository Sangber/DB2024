from django.db import models

# Create your models here.
class student(models.Model):
    sid         = models.CharField(max_length = 32, unique = True)
    sname       = models.CharField(max_length = 32)
    gender      = models.CharField(max_length = 32)
    birth_date  = models.CharField(max_length = 32)
    major_id    = models.CharField(max_length = 32)