from django.db import models
from django.contrib.auth import get_user_model

from shop.models import Product

user = get_user_model()

class Basket(models.Model):
    """User shopping basket"""
    user = models.ForeignKey(user, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
