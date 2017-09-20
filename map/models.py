# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

class CentrosAcopio(models.Model):
    nombre = models.CharField(max_length=500)
    lugar = models.TextField()
    colonia = models.CharField(max_length=500)
    lat = models.IntegerField(null=True)
    lon = models.IntegerField(null=True)
    entidad = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre

class Desastres(models.Model):
    tipo = models.CharField(max_length=500)
    atrapados = models.IntegerField(null=True)
    lesionados = models.IntegerField(null=True)
    desaparecidos = models.IntegerField(null=True)
    fallecidos = models.IntegerField(null=True)
    rescatados = models.IntegerField(null=True)
    entidad = models.CharField(max_length=200)
    lat = models.IntegerField(null=True)
    lon = models.IntegerField(null=True)

    def __str__(self):
        return self.tipo

class Albergues(models.Model):
    direccion = models.TextField()
    entidad = models.CharField(max_length=200)
    lat = models.IntegerField(null=True)
    lon = models.IntegerField(null=True)

    def __str__(self):
        return self.tipo
