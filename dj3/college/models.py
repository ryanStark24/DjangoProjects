from django.db import models


# Create your models here.
class College(models.Model):
    subject = models.CharField(max_length=200)
    message = models.TextField()
    cr_date = models.DateField()
    
