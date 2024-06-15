# accounts/models.py
from django.contrib.auth.models import User
from django.db import models

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_wholesale = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username
from django.db import models

# Create your models here.
