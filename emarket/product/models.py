from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.TextChoices):
    COMPUTER = "Computer"
    MOBILE = "Mobile"
    FOOD = "Food"
    HOME = "Home"

class Product(models.Model):
    name = models.CharField(max_length=100, default="", blank=False, null=False)
    description = models.TextField(max_length=1000, default="", blank=False, null=False)
    price = models.DecimalField(max_digits=7, decimal_places=2, default=0.00, blank=False, null=False)
    brand = models.CharField(max_length=200, default="", blank=False, null=False)
    category = models.CharField(max_length=40, choices=Category.choices, default=Category.COMPUTER, blank=False, null=False)
    rating = models.DecimalField(max_digits=3,decimal_places=2, default=0.00)
    stock = models.IntegerField(default="0")
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'