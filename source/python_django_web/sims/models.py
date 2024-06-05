from django.db import models

# Create your models here.
class major(models.Model):
    mid     = models.CharField(max_length = 32, unique = True)
    mname   = models.CharField(max_length = 32)

class student(models.Model):
    sid         = models.CharField(max_length = 32, unique = True)
    sname       = models.CharField(max_length = 32)
    gender      = models.CharField(max_length = 32)
    birth_date  = models.CharField(max_length = 32)
    major_id    = models.CharField(max_length = 32)

class course(models.Model):
    cid         = models.CharField(max_length = 32, unique = True)
    cname       = models.CharField(max_length = 32)
    major_id    = models.CharField(max_length = 32)