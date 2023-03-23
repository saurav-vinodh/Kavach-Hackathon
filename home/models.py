from django.db import models

# Create your models here.

class Entry(models.Model):
    

    contact = models.CharField(max_length=200)
    source = models.CharField(max_length=200)
    weight= models.IntegerField(default=1)
    date = models.DateTimeField(auto_now_add=True)
    userid = models.AutoField(primary_key=True)
    risk_score = models.IntegerField()
    spam = models.IntegerField()

    
    class Meta:
        unique_together=('userid', 'contact',)

