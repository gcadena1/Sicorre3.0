from django.db import models

# Create your models here.
class RH_Organigrama(models.Model):
    usuario = models.CharField(max_length=200)   
    nombre = models.CharField(max_length=200)   
    class Meta:
        db_table="usuario"