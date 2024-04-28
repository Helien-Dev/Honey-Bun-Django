from django.contrib.auth.models import User
from django.utils.text import slugify
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings


# Create your models here.
class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    password = models.CharField(max_length=200, null=True)
    first_name = models.CharField(max_length=200, null=True)
    last_name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=300, null=True)

    @receiver(post_save, sender=User)
    def create_or_update_customer(sender, instance, created, **kwargs):
        if created:
            try:
                Customer.objects.create(
                    user=instance,
                    email=instance.email,
                    first_name=instance.first_name,
                    last_name=instance.last_name,
                )
            except Exception as e:
                print(f"Error trying to create customer: {e}")
        else:
            try:
                instance.customer.email = instance.email
                instance.customer.first_name = instance.first_name
                instance.customer.last_name = instance.last_name
                instance.customer.save()
            except Exception as e:
                print(f"Error trying to update customer: {e}")

    def __str__(self):
        return self.first_name


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

    DEFAULT_IMAGE_URL = settings.MEDIA_URL + "/not_image_found.jpg"

    @property
    def ImageURL(
        self,
    ):
        try:
            url = self.image.url
        except:
            url = self.DEFAULT_IMAGE_URL
        return url

    def __str__(self):
        return self.name


class Order(models.Model):
    customer = models.ForeignKey(
        Customer, on_delete=models.SET_NULL, null=True, blank=True
    )
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False)
    transaction_id = models.CharField(max_length=100, null=True)

    def __str__(self) -> str:
        return str(self.id)


class OrderItem(models.Model):
    product = models.ForeignKey(
        Product, on_delete=models.SET_NULL, null=True, blank=True
    )
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True, blank=True)
    quantity = models.PositiveIntegerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)


class ShippingAddress(models.Model):
    customer = models.ForeignKey(
        Customer, on_delete=models.SET_NULL, null=True, blank=True
    )
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True, blank=True)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    zip = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.address
