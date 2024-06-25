from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='products/')

    def __str__(self):
        return self.name

class Variety(models.Model):
    product = models.ForeignKey(Product, related_name='varieties', on_delete=models.CASCADE)
    name = models.CharField(max_length=255, default='Default Name')
    description = models.TextField()
    image = models.ImageField(upload_to='varieties/')
    stock = models.IntegerField()
    retail_price = models.DecimalField(max_digits=10, decimal_places=2)
    wholesale_price = models.DecimalField(max_digits=10, decimal_places=2)


    def __str__(self):
        return self.name

'''class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_wholesale = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_customer_profile(sender, instance, created, **kwargs):
    if created:
        Customer.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_customer_profile(sender, instance, **kwargs):'''