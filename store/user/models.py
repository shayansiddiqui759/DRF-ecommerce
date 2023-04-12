from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    contact_number = models.IntegerField(blank=True)
    address = models.CharField(max_length=100,blank=True)

    def __str__(self):
        return self.username