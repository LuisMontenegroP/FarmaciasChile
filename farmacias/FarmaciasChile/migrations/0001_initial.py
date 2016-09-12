# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-09-12 01:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Farmacias',
            fields=[
                ('local_id', models.IntegerField(primary_key=True, serialize=False)),
                ('local_nombre', models.TextField(blank=True, null=True)),
                ('comuna_nombre', models.TextField(blank=True, null=True)),
                ('localidad_nombre', models.TextField(blank=True, null=True)),
                ('local_direccion', models.TextField(blank=True, null=True)),
                ('funcionamiento_hora_apertura', models.TextField(blank=True, null=True)),
                ('funcionamiento_hora_cierre', models.TextField(blank=True, null=True)),
                ('local_telefono', models.TextField(blank=True, null=True)),
                ('local_lat', models.TextField(blank=True, null=True)),
                ('local_lng', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'farmacias',
                'managed': False,
            },
        ),
    ]