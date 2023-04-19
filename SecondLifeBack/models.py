from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    birthday = models.DateField(null=True)
   
    def __str__(self):
        return self.username

class Listing(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

