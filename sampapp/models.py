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
    autorizacion = models.ForeignKey(Autorizacion, blank=True, null=True)
    descripcion = models.CharField(max_length=255)
    fechainicio = models.DateField('fecha de finalizacion')
    fechafin = models.DateField('fecha de inicio')
    nombre = models.CharField(max_length=255)
    programa = models.ForeignKey('Programa')
    destinatario = models.ForeignKey('Destinatario')
    class Meta:
        managed = True

class Autorizacion(models.Model):
    descripcion = models.CharField(max_length=255)
    estado = models.BooleanField()
    dependencia = models.ForeignKey('Dependencia')
    class Meta:
        managed = True
        

class Dependencia(models.Model):
    descripcion = models.CharField(max_length=255)
    nombre = models.CharField(max_length=255)    
    dependencia = models.ForeignKey('self', blank=True, null=True)
    responsable = models.ForeignKey('Responsable', blank=True, null=True)
    class Meta:
        managed = True        

class Destinatario(models.Model):
    descripcion = models.CharField(max_length=255)
    class Meta:
        managed = True
                

class Escuela(models.Model):
    ambito = models.CharField(max_length=255) """
    Urbano
 Rural
 Rural Aglomerado
 Rural Disperso
 No Corresponde"""
    anexo = models.IntegerField()
    codjurisdiccional = models.CharField('codigo jurisdiccional',max_length=255)
    cue = models.IntegerField()
    dependencia = models.CharField(max_length=255) # municipal, provincial, nacional 
    direccion = models.CharField(max_length=255)
    fechacreacion = models.DateField(default=timezone.now)
    estado = models.BooleanField(default=True)
    nombre = models.CharField(max_length=255)
    sector = models.CharField(max_length=255) # estatal, privado
    nivel = models.CharField(max_length=255) # comun, especial, adultos
    orientacion = models.CharField(max_length=255) 
    """
 No corresponde
 Bachiller
 Ciclo Básico
 Comercial
 Técnica
 Agropecuaria
 Artística
 Otros
 Ciclo Básico Técnico
 Humanidades y Cs. Sociales
 Lenguas
 Ciencias Naturales
 Ciencias naturales, salud y medio ambiente
 Economía y Gestión de las Organizaciones
 Economía y Administración
 Informática
 Gestión y Administración
 Tecnología
 Producción de Bienes y Servicios
 Comuncación, Artes y Diseño
 Ciclo Básico Artístico
 Comunicación
 Ciclo Básico Agrario
 Agro y Ambiente
 Turismo
 Educación Física
 """
    localidad = models.ForeignKey(Localidad, blank=True, null=True)
    class Meta:
        managed = True
        

class Fondos(models.Model):
    monto = models.FloatField() 
    tipofinanciacion = models.CharField('tipo de financiacion',max_length=255) #Provincia o nación
    class Meta:
        managed = True
        

class Instrumentolegal(models.Model):
    descripcion = models.CharField(max_length=255)
    fecha = models.DateField()
    tipodocleg = models.CharField('tipo de documento legal',max_length=255)
    class Meta:
        managed = True
        

class Localidad(models.Model):
    codigopostal = models.IntegerField('codigo postal')
    departamento = models.CharField(max_length=255)
    nombre = models.CharField(max_length=255)
    region = models.CharField(max_length=255) # 123456
    accion = models.ForeignKey(Accion, blank=True, null=True)
    escuela = models.ForeignKey(Escuela, blank=True, null=True)
    class Meta:
        managed = True
        

class Persona(models.Model):
    apellido = models.CharField(max_length=255)
    direccion = models.CharField(max_length=255)
    tipodocumento = models.CharField() # dni, etc.
    documento = models.IntegerField()
	cuilcuit = models.CharField()
	fechanacimiento = models.DateField()
    edad = models.IntegerField()
    nacionalidad = models.CharField(max_length=255)
    nombre = models.CharField(max_length=255)
    localidad = models.ForeignKey(Localidad, blank=True, null=True)
    email = models.CharField('e-mail',max_length=255)
    fax = models.CharField(max_length=255)
    interno = models.CharField(max_length=255)
    red = models.CharField(max_length=255)
    telefono = models.CharField(max_length=255)
    situacionlaboral = models.ForeignKey(Situacionlaboral)
    class Meta:
        managed = True
        db_table = 'persona'

class Programa(models.Model):    
    descripcion = models.CharField(max_length=255)
    direccion = models.CharField(max_length=255)
    fechacreacion = models.DateField('fecha de creacion')
    mision = models.CharField(max_length=255)
    nombre = models.CharField(max_length=255)
    contacto = models.ForeignKey(Contacto, blank=True, null=True)
    equipotrabajo = models.ForeignKey(Equipotrabajo, blank=True, null=True)
    fondos = models.ForeignKey(Fondos, blank=True, null=True)
    instrumentolegal = models.ForeignKey(Instrumentolegal, blank=True, null=True)
    dependencia = models.ForeignKey(Dependencia, blank=True, null=True)
    email = models.CharField('e-mail',max_length=255)
    fax = models.CharField(max_length=255)
    interno = models.CharField(max_length=255)
    red = models.CharField(max_length=255)
    telefono = models.CharField(max_length=255)
    destinatario = models.ForeignKey(Destinatario)
    fondo = models.ForeignKey(Fondo)
    class Meta:
        managed = True
        db_table = 'programa'

class Rol(Persona):    
    class Meta:
    	abstract = True
        managed = True

class Responsable(Rol):    
    class Meta:
        managed = True

class Agente(Rol):    
    class Meta:
        managed = True

class Situacionlaboral(models.Model):    
    codigocargo = models.IntegerField('codigo de cargo')
    descripcion = models.CharField(max_length=255)
    fechaingreso = models.DateField('fecha de ingreso')
    tipocargo = models.CharField('tipo de cargo',max_length=1)    
    class Meta:
        managed = True
        db_table = 'situacionlaboral'

class Tarea(models.Model):    
    descripcion = models.CharField(max_length=255)
    fechafin = models.DateField('fecha de finalizacion')
    fechainicio = models.DateField('fecha de inicio')
    nombre = models.CharField(max_length=255)
    prioridad = models.IntegerField()
    accion = models.ForeignKey(Accion, blank=True, null=True)
    rol = models.ForeignKey(Rol, blank=True, null=True)
    class Meta:
        managed = True
        db_table = 'tarea'



