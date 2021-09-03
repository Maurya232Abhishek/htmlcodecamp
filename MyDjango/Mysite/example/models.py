from django.db import models

# Create your models here.
class Book(models.Model):
    name=models.CharField(max_length=50)
    bid= models.CharField(max_length=8)
    author= models.CharField(max_length=50)
    price= models.IntegerField()
class Meta:
    db_table = "Library"
