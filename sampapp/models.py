# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.
from __future__ import unicode_literals

from django.db import models

class Accion(models.Model):
    id = models.BigIntegerField(primary_key=True)
    descripcion = models.CharField(max_length=255)
    fechafin = models.DateField()
    fechainicio = models.DateField()
    idaccion = models.IntegerField()
    nombre = models.CharField(max_length=255)
    programa = models.ForeignKey('Programa')
    class Meta:
        managed = False
        db_table = 'accion'

class Autorizacion(models.Model):
    id = models.BigIntegerField(primary_key=True)
    descripcion = models.CharField(max_length=255)
    idautorizacion = models.IntegerField()
    accion = models.ForeignKey(Accion, blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'autorizacion'

class Contacto(models.Model):
    id = models.BigIntegerField(primary_key=True)
    email = models.CharField(max_length=255)
    fax = models.CharField(max_length=255)
    idcontacto = models.IntegerField()
    interno = models.CharField(max_length=255)
    red = models.CharField(max_length=255)
    telefono = models.CharField(max_length=255)
    class Meta:
        managed = False
        db_table = 'contacto'

class Dependencia(models.Model):
    id = models.BigIntegerField(primary_key=True)
    descripcion = models.CharField(max_length=255)
    iddependencia = models.IntegerField()
    nombre = models.CharField(max_length=255)
    autorizacion = models.ForeignKey(Autorizacion, blank=True, null=True)
    programa = models.ForeignKey('Programa', blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'dependencia'

class Destinatario(models.Model):
    id = models.BigIntegerField(primary_key=True)
    descripcion = models.CharField(max_length=255)
    iddestinatario = models.IntegerField()
    accion = models.ForeignKey(Accion, blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'destinatario'

class Equipotrabajo(models.Model):
    id = models.BigIntegerField(primary_key=True)
    descripcion = models.CharField(max_length=255)
    fechacreacion = models.DateField()
    idequipotrabajo = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'equipotrabajo'

class Escuela(models.Model):
    id = models.BigIntegerField(primary_key=True)
    ambito = models.CharField(max_length=255)
    anexo = models.IntegerField()
    codjurisdiccional = models.CharField(max_length=255)
    cue = models.IntegerField()
    dependencia = models.CharField(max_length=255)
    direccion = models.CharField(max_length=255)
    idescuela = models.IntegerField()
    nombre = models.CharField(max_length=255)
    sector = models.CharField(max_length=255)
    class Meta:
        managed = False
        db_table = 'escuela'

class Fondos(models.Model):
    id = models.BigIntegerField(primary_key=True)
    idfondo = models.IntegerField()
    monto = models.TextField() # This field type is a guess.
    tipofinanc = models.CharField(max_length=255)
    class Meta:
        managed = False
        db_table = 'fondos'

class Instrumentolegal(models.Model):
    id = models.BigIntegerField(primary_key=True)
    descripcion = models.CharField(max_length=255)
    fecha = models.DateField()
    idinstrumentolegal = models.IntegerField()
    tipodocleg = models.CharField(max_length=255)
    class Meta:
        managed = False
        db_table = 'instrumentolegal'

class Localidad(models.Model):
    id = models.BigIntegerField(primary_key=True)
    codigopostal = models.IntegerField()
    departamento = models.CharField(max_length=255)
    idlocalidad = models.IntegerField()
    nombre = models.CharField(max_length=255)
    region = models.CharField(max_length=255)
    accion = models.ForeignKey(Accion, blank=True, null=True)
    escuela = models.ForeignKey(Escuela, blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'localidad'

class Nivel(models.Model):
    id = models.BigIntegerField(primary_key=True)
    codigonivel = models.CharField(max_length=1)
    descripcion = models.CharField(max_length=255)
    idnivel = models.IntegerField()
    escuela = models.ForeignKey(Escuela, blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'nivel'

class Persona(models.Model):
    id = models.BigIntegerField(primary_key=True)
    apellido = models.CharField(max_length=255)
    direccion = models.CharField(max_length=255)
    dni = models.IntegerField()
    edad = models.IntegerField()
    idpersona = models.IntegerField()
    nacionalidad = models.CharField(max_length=255)
    nombre = models.CharField(max_length=255)
    contacto = models.ForeignKey(Contacto, blank=True, null=True)
    localidad = models.ForeignKey(Localidad, blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'persona'

class Programa(models.Model):
    id = models.BigIntegerField(primary_key=True)
    descripcion = models.CharField(max_length=255)
    direccion = models.CharField(max_length=255)
    fechacreacion = models.DateField()
    idprograma = models.IntegerField()
    mision = models.CharField(max_length=255)
    nombre = models.CharField(max_length=255)
    contacto = models.ForeignKey(Contacto, blank=True, null=True)
    equipotrabajo = models.ForeignKey(Equipotrabajo, blank=True, null=True)
    fondos = models.ForeignKey(Fondos, blank=True, null=True)
    instrumentolegal = models.ForeignKey(Instrumentolegal, blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'programa'

class ProgramaAccion(models.Model):
    programa = models.ForeignKey(Programa)
    accion = models.ForeignKey(Accion, unique=True)
    class Meta:
        managed = False
        db_table = 'programa_accion'

class Rol(models.Model):
    dtype = models.CharField(max_length=31)
    id = models.BigIntegerField(primary_key=True)
    idrol = models.IntegerField()
    idresponsable = models.IntegerField()
    idagente = models.IntegerField()
    persona = models.ForeignKey(Persona, blank=True, null=True)
    programa = models.ForeignKey(Programa, blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'rol'

class Situacionlaboral(models.Model):
    id = models.BigIntegerField(primary_key=True)
    codigocargo = models.IntegerField()
    descripcion = models.CharField(max_length=255)
    fechaingreso = models.DateField()
    idsituacionlaboral = models.IntegerField()
    tipocargo = models.CharField(max_length=1)
    persona = models.ForeignKey(Persona, blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'situacionlaboral'

class Tarea(models.Model):
    id = models.BigIntegerField(primary_key=True)
    descripcion = models.CharField(max_length=255)
    fechafin = models.DateField()
    fechainicio = models.DateField()
    idtarea = models.IntegerField()
    nombre = models.CharField(max_length=255)
    prioridad = models.IntegerField()
    accion = models.ForeignKey(Accion, blank=True, null=True)
    rol = models.ForeignKey(Rol, blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'tarea'



