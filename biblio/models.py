from datetime import date
from typing import Optional
from django.db import models
from django.contrib.auth.models import AbstractUser
 
class Llibre (models.Model):
    titol = models.CharField(max_length=100)
    autor = models.CharField(max_length=200)
    resum = models.TextField(null=True,blank=True)
    data_edicio = models.DateField(null=True, blank=True)
    imatge = models.ImageField(upload_to='imatges/', null=True, blank=True)

    def __str__(self):
        return self.titol + " - " + self.autor
    
class Usuari(AbstractUser):
    auth_token = models.CharField(max_length=32,blank=True,null=True)


# modelo imagen q puede ser de un libro.
class Imatge(models.Model):
    llibre = models.ForeignKey(Llibre, on_delete=models.CASCADE, related_name='imatges')
    imatge = models.ImageField(upload_to='imatges/', null=True, blank=True)

    def __str__(self):
        return f"Imatge de {self.llibre.titol}"
