from django.db import models
from django.urls import reverse


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    level = models.IntegerField()
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name


class Seller(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.SET(1), default='1')
    name = models.CharField(max_length=300)
    count = models.IntegerField()
    price = models.IntegerField(default=0)
    description = models.TextField()
    is_to_order = models.BooleanField(default="False")
    image = models.ImageField(null=True, blank=True, upload_to="images/")
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE, null=True, default=None)

    def __str__(self):
        return self.name

    # redirect from adding
    def get_absolute_url(self):
        return reverse('detail', args=[self.id])
