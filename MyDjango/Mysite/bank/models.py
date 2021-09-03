from django.db import models

# Create your models here.
class AccountDetail(models.Model):
    accno= models.CharField(max_length=13)
    name= models.CharField(max_length=50)
    balance= models.IntegerField()
    
    class Meta():
        db_table="Bank"