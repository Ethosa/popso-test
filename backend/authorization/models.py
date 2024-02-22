from django.db import models



class User(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    login = models.CharField(max_length=32)
    password = models.CharField(max_length=256)
