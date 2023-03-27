from django.db import models

# Create your models here.

class Entry(models.Model):
    

    contact = models.CharField(max_length=200)
    source = models.CharField(max_length=200)
    weight= models.IntegerField(default=1)
    date = models.DateTimeField(auto_now_add=True)
    userid = models.CharField(max_length=200, default='Saurav')
    risk_score = models.IntegerField()
    spam = models.IntegerField()
    subject = models.CharField(max_length = 10000, blank=True)
    body = models.CharField(max_length = 10000, blank=True)
    sms = models.CharField(max_length = 10000, blank=True)

    class Meta:
        unique_together=('userid', 'contact',)

