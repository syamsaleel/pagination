
# Create your models here.
from django.db import models

# Create your models here.
class Product(models.Model):
    titile=models.CharField(max_length=100)
    description=models.CharField(max_length=200)
    Company=models.CharField(max_length=100)
    created=models.DateTimeField(auto_now_add=True)
