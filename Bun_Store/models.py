from django.contrib.auth.models import User
from django.utils.text import slugify
from django.db import models


# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.FloatField()
    digital = models.BooleanField(default=False, null=True, blank=True)
    product_description = models.TextField(max_length=400, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    alt = models.TextField(max_length=100, null=True, blank=True)
    slug = models.SlugField(unique=True, null=True, blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
