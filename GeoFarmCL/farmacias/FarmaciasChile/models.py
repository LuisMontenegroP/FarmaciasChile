from __future__ import unicode_literals

from django.db import models

class Farmacias(models.Model):
    local_nombre = models.CharField(blank=True, null=True, max_length=200)
    comuna_nombre = models.CharField(blank=True, null=True, max_length=200)
    localidad_nombre = models.CharField(blank=True, null=True, max_length=200)
    local_direccion = models.CharField(blank=True, null=True, max_length=200)
    funcionamiento_hora_apertura = models.CharField(blank=True, null=True, max_length=200)
    funcionamiento_hora_cierre = models.CharField(blank=True, null=True, max_length=200)
    local_telefono = models.CharField(blank=True, null=True, max_length=200)
    local_lat = models.IntegerField(blank=True, null=True)
    local_lng = models.IntegerField(blank=True, null=True)
    medicamento = models.CharField(blank=True, null=True, max_length=200)
    precio = models.IntegerField(blank=True, null=True)

    class Meta:
        ordering = ["local_nombre"]
        managed = False
        db_table = 'farmacias'
