from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class City(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Advert(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    capacity = models.PositiveIntegerField(default=0)  
    source = models.ForeignKey(City, on_delete=models.CASCADE, related_name='source_adverts', blank=True, null=True)
    destination = models.ForeignKey(City, on_delete=models.CASCADE, related_name='destination_adverts', blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='adverts')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='adverts')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
