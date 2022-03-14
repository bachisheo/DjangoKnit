from django.db import models


# Create your models here.
class Category(models.Model):
    id = models.IntegerField(primary_key=True, auto_created=True)
    name = models.CharField(max_length=50)
    level = models.IntegerField()


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.SET(1))
    id = models.IntegerField(primary_key=True, auto_created=True)
    name = models.CharField(max_length=300)
    count = models.IntegerField()
    price = models.IntegerField(default=0)
    description = models.TextField()
    is_to_order = models.BooleanField()
