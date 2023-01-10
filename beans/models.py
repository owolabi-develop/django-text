from pyexpat import model
from django.db import models

# Create your models here.

class Product(models.Model):
    Name = models.CharField(max_length=255)
    Price = models.IntegerField(max_length=244)

    def __str__(self) -> str:
        return " %s " % self.Name 