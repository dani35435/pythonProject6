from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=254)
    desk = models.TextField(max_length=254)
    image = models.ImageField(upload_to='media/')

    def __str__(self):
        return self.name