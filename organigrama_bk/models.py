from django.db import models

class organigrama(models.Model):
    usuario = models.CharField(max_length=200)   
    class Meta:
        db_table="usuario"
