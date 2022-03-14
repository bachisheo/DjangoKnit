from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    level = models.IntegerField()
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.SET(1))
    name = models.CharField(max_length=300)
    count = models.IntegerField()
    price = models.IntegerField(default=0)
    description = models.TextField()
    is_to_order = models.BooleanField()

    def __str__(self):
        return self.name
