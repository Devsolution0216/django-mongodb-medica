# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.core.validators import RegexValidator

from mongoengine import *


# Create your models here.
class Data(models.Model):
    id_cilab = models.IntegerField()
    nombres = models.CharField(max_length=40)
    escolaridad = models.CharField(max_length=40)
    fec_nac = models.CharField(max_length=40)
    c_p_nac = models.IntegerField()
    empresa = models.CharField(max_length=40)
    no_emp = models.IntegerField()
    apellido_p = models.CharField(max_length=40)
    genero = models.IntegerField()
    edad = models.CharField(max_length=40)
    c_p_actual = models.IntegerField()
    depto = models.CharField(max_length=40)
    fecha = models.CharField(max_length=40)
    apellido_m = models.CharField(max_length=40)
    edo_civil = models.CharField(max_length=40)
    c_p_trabajo = models.IntegerField()
    puesto = models.CharField(max_length=40)
    created_at = models.DateTimeField('%m/%d/%Y %H:%M:%S')
    updated_at = models.DateTimeField('%m/%d/%Y %H:%M:%S')

