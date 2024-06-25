from django.db import models
from django.contrib.auth.models import User
from products.models import Variety
from accounts.models import Customer

class Order(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    variety = models.ForeignKey(Variety, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    order_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order #{self.id} by {self.customer.username}"