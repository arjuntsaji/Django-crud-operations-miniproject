from django.db import models

# Create your models here.


class Profile(models.Model):
    auth_token = models.CharField(max_length=100)
