from django.db import models
from django.urls.base import reverse


# Create your models here.
class College(models.Model):
    subject = models.CharField(max_length=200)
    message = models.TextField()
    cr_date = models.DateField()
    def get_absolute_url(self):
        return reverse('college:index')
    
