from django.db import models

class User(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, blank=False, default='')
    username = models.CharField(max_length=200, blank=False, default='')
    email = models.CharField(max_length=200, blank=False, default='')
    password = models.CharField(max_length=200, blank=False, default='')
    role_id = models.BigIntegerField(blank=False, default=1)

