from __future__ import unicode_literals

from django.db import models
	
class Farmacias(models.Model):
    local_id = models.IntegerField(primary_key=True)
    local_nombre = models.TextField(blank=True, null=True)
    comuna_nombre = models.TextField(blank=True, null=True)
    localidad_nombre = models.TextField(blank=True, null=True)
    local_direccion = models.TextField(blank=True, null=True)
    funcionamiento_hora_apertura = models.TextField(blank=True, null=True)
    funcionamiento_hora_cierre = models.TextField(blank=True, null=True)
    local_telefono = models.TextField(blank=True, null=True)
    local_lat = models.TextField(blank=True, null=True)
    local_lng = models.TextField(blank=True, null=True)

    def __unicode__(self):
		return self.local_nombre

    class Meta:
        managed = False
        db_table = 'farmacias'