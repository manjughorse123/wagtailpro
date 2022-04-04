from tabnanny import verbose
from django.db import models

# Create your models here.


class Subcriber(models.Model):
    email = models.CharField(max_length=100, blank=False, null= False)
    full_name = models.CharField(max_length=100, blank=False, null= False)

    def __str__(self):

        return self.full_name
    
    class Meta:
        verbose_name = "Subcriber"
        verbose_name_plural = "Subcribers"