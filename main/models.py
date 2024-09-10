from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()
    fat_content = models.CharField(max_length=50)
    quantity = models.IntegerField()
    rating = models.DecimalField(max_digits=3, decimal_places=2)