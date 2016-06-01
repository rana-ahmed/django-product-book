from django.db import models

class Product(models.Model):
    name = models.CharField(max_length = 120)
    price = models.FloatField()
    stock = models.FloatField()
    unit = models.CharField(max_length = 10)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.name
