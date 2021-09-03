from django.db import models
#quiztest
# Create your models here.
class quizClass(models.Model):
    qno= models.IntegerField()
    que= models.CharField(max_length=200)
    opta= models.CharField(max_length=200)
    optb= models.CharField(max_length=200)
    optc= models.CharField(max_length=200)
    optd= models.CharField(max_length=200)
    rightans= models.IntegerField()
    
    class Meta():
        db_table="questions"
