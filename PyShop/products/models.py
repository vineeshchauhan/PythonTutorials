from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    stock = models.IntegerField()
    image_url = models.CharField(max_length=2083)
    objects = models.Manager()  # Ensure default manager exists

class Offer(models.Model):
    code = models.CharField(max_length=50)
    description = models.CharField(max_length=250)
    discount = models.FloatField()