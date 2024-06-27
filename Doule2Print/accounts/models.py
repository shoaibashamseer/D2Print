# accounts/models.py
from django.contrib.auth.models import User
from django.db import models

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Add a field to store customer type
    CUSTOMER_TYPES = [
        ('RETAIL', 'Retail'),
        ('WHOLESALE', 'Wholesale'),
    ]
    customer_type = models.CharField(max_length=10, choices=CUSTOMER_TYPES)

    def __str__(self):
        return self.user.username
