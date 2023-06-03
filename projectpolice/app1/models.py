from django.db import models
class Challan(models.Model):
    sno=models.IntegerField()
    owner=models.CharField(max_length=50)
    vehicle=models.CharField(max_length=50)
    date=models.DateField()
    amount=models.IntegerField()
# Create your models here.
