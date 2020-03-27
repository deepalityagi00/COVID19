from django.db import models
from datetime import datetime 

# Create your models here.
class Country(models.Model):
    date = models.DateTimeField(default=datetime.now())
    name = models.CharField(max_length=50)
    new = models.PositiveIntegerField()
    deaths = models.PositiveIntegerField()
    recovered = models.PositiveIntegerField()
    active = models.PositiveIntegerField()
    total = models.PositiveIntegerField()    

    class Meta:
        unique_together=("date","name")

class CoronaSpread(models.Model):
    Countries = models.ManyToManyField(Country,related_name="world")
    date = models.DateTimeField(default=datetime.now())
    new = models.PositiveIntegerField()
    deaths = models.PositiveIntegerField()
    recovered = models.PositiveIntegerField()
    active = models.PositiveIntegerField()
    total = models.PositiveIntegerField()

    class Meta:
        unique_together=("date","total")
