from django.db import models
import django
import datetime

# Create your models here.

class Kriskras(models.Model):
    tak = models.CharField(max_length=20)


    def __str__(self):
        return self.tak

class Vergadering(models.Model):
    kriskras = models.ForeignKey(Kriskras, on_delete=models.CASCADE)
    date = models.DateField(("Date"), default=datetime.date.today)
    extra = models.CharField(max_length=5)
    activiteit = models.CharField(max_length=500)

    def __str__(self):
        return self.activiteit



    
    
    
