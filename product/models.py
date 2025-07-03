from django.db import models

from django.db import models

class Product(models.Model):
    image = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    sale = models.CharField(max_length=10, blank=True)
    isnew = models.BooleanField(default=False)
    category = models.CharField(max_length=100)
    price_new = models.DecimalField(max_digits=10, decimal_places=2)
    price_old = models.DecimalField(max_digits=10, decimal_places=2)
    rating = models.PositiveSmallIntegerField(default=0)
    topselling = models.BooleanField(default=False)

    def __str__(self):
        return self.name