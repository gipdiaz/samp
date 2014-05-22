# -*- coding: utf-8 -*-
from django.db import models
from django.utils import timezone

# ---------------------- #
class Accion(models.Model):
    autorizacion = models.ForeignKey("Autorizacion", blank=True, null=True)
    descripcion = models.CharField(max_length=255)
    fechainicio = models.DateField('fecha de finalizacion')
    fechafin = models.DateField('fecha de inicio')
    nombre = models.CharField(max_length=255)
    programa = models.ForeignKey('Programa')
    destinatario = models.ForeignKey('Destinatario')
    fecha_creacion = models.DateTimeField(default = timezone.now())
    
    class Meta:
        verbose_name_plural = "Acciones"

    def __unicode__(self):
        return u'%s' % (self.nombre)

# ---------------------- #
class Autorizacion(models.Model):
    descripcion = models.CharField(max_length=255)
    estado = models.BooleanField()
    dependencia = models.ForeignKey('Dependencia')
    fecha_creacion = models.DateTimeField(default = timezone.now())
    
    class Meta:
        verbose_name_plural = "Autorizaciones"

    def __unicode__(self):
        return u'%s' % (self.descripcion)
        
# ---------------------- #
class Dependencia(models.Model):
    descripcion = models.CharField(max_length=255)
    nombre = models.CharField(max_length=255)    
    dependencia = models.ForeignKey('self', related_name="depende", blank=True, null=True)
    responsable = models.ForeignKey('Responsable', blank=True, null=True)
    fecha_creacion = models.DateTimeField(default = timezone.now())
    
    class Meta:
        verbose_name_plural = "Dependencias"

    def __unicode__(self):
        return u'%s' % (self.descripcion)        

# ---------------------- #
class Destinatario(models.Model):
    descripcion = models.CharField(max_length=255)
    fecha_creacion = models.DateTimeField(default = timezone.now())
    
    class Meta:
        verbose_name_plural = "Destinatarios"

    def __unicode__(self):
        return u'%s' % (self.descripcion)
                
# ---------------------- #
class Escuela(models.Model):
    
    TIPO_AMBITO = (
        (0, "Urbano"),
        (1, "Rural"),
        (2, "Rural Aglomerado"),
        (3, "Rural Disperso"),
        (4, "No Corresponde")
    )

    ORIENTACION = (
        (0, "No corresponde"),
        (1, "Bachiller"),
        (2, "Ciclo Básico"),
        (3, "Comercial"),
        (4, "Técnica"),
        (5, "Agropecuaria"),
        (6, "Artística"),
        (7, "Otros"),
        (8, "Ciclo Básico Técnico"),
        (9, "Humanidades y Cs. Sociales"),
        (10, "Lenguas"),
        (11, "Ciencias Naturales"),
        (12, "Ciencias naturales, salud y medio ambiente"),
        (13, "Economía y Gestión de las Organizaciones"),
        (14, "Economía y Administración"),
        (15, "Informática"),
        (16, "Gestión y Administración"),
        (17, "Tecnología"),
        (18, "Producción de Bienes y Servicios"),
        (19, "Comuncación, Artes y Diseño"),
        (20, "Ciclo Básico Artístico"),
        (21, "Comunicación"),
        (22, "Ciclo Básico Agrario"),
        (23, "Agro y Ambiente"),
        (24, "Turismo"),
        (25, "Educación Física")
    )

    DEPENDENCIA = (
        (0, "Municipal"),
        (1, "Provincial"),
        (2, "Nacional")
    )

    SECTOR = (
        (0, "Estatal"),
        (1, "Privado",)
    )

    NIVEL = (
        (0, "Común"),
        (1, "Especial",),
        (2, "Adultos")
    )
    
    TIPO_AMBITO_DICT = dict(TIPO_AMBITO)
    ORIENTACION_DICT = dict(ORIENTACION)
    DEPENDENCIA_DICT = dict(DEPENDENCIA)
    SECTOR_DICT = dict(SECTOR)
    NIVEL_DICT = dict(NIVEL)
    
    tipo_ambito = models.PositiveSmallIntegerField(choices = TIPO_AMBITO)
    ambito = models.CharField(max_length=255)
    anexo = models.IntegerField()
    codjurisdiccional = models.CharField('codigo jurisdiccional',max_length=255)
    cue = models.IntegerField()
    dependencia = models.PositiveSmallIntegerField(choices = DEPENDENCIA)
    direccion = models.CharField(max_length=255)
    estado = models.BooleanField(default=True)
    nombre = models.CharField(max_length=255)
    sector = models.PositiveSmallIntegerField(choices = SECTOR)
    nivel = models.PositiveSmallIntegerField(choices = NIVEL)
    orientacion = models.PositiveSmallIntegerField(choices = ORIENTACION)
    localidad = models.ForeignKey("Localidad", blank=True, null=True)
    fecha_creacion = models.DateTimeField(default = timezone.now())

    class Meta:
        verbose_name_plural = "Escuelas"

    def __unicode__(self):
        return u'%s' % (self.nombre)
        
# ---------------------- #
class Fondo(models.Model):

    TIPO_FINANCIACION = (
        (0, "Provincia"),
        (1, "Nacion")
    )
    
    TIPO_FINANCIACION_DICT = dict(TIPO_FINANCIACION)

    descripcion = models.CharField(max_length=255)
    monto = models.FloatField() 
    tipofinanciacion = models.PositiveSmallIntegerField(choices = TIPO_FINANCIACION)
    fecha_creacion = models.DateTimeField(default = timezone.now())
    
    class Meta:
        verbose_name_plural = "Fondos"

    def __unicode__(self):
        return u'%s' % (self.descripcion)
        
# ---------------------- #
class Instrumentolegal(models.Model):
    descripcion = models.CharField(max_length=255)
    tipodocleg = models.CharField('tipo de documento legal',max_length=255)
    fecha_creacion = models.DateTimeField(default = timezone.now())
    
    class Meta:
        verbose_name_plural = "Instrumentos Legales"

    def __unicode__(self):
        return u'%s' % (self.descripcion)

# ---------------------- #
class Localidad(models.Model):

    REGION = (
        (1, "I"),
        (2, "II"),
        (3, "III"),
        (4, "IV"),
        (5, "V"),
        (6, "VI")
    )

    REGION_DICT = dict(REGION)

    codigopostal = models.IntegerField('codigo postal')
    departamento = models.CharField(max_length=255)
    nombre = models.CharField(max_length=255)
    region = models.PositiveSmallIntegerField(choices = REGION)
    accion = models.ForeignKey(Accion, blank=True, null=True)
    fecha_creacion = models.DateTimeField(default = timezone.now())
    
    class Meta:
        verbose_name_plural = "Localidades"

    def __unicode__(self):
        return u'%s' % (self.nombre)
        
# ---------------------- #
class Persona(models.Model):

    TIPO_DOCUMENTO = (
        (0, "DNI"),
        (1, "LC"),
        (2, "LE"),
        (3, "CI"),
        (4, "Pasaporte")
    )

    TIPO_DOCUMENTO_DICT = dict(TIPO_DOCUMENTO)

    apellido = models.CharField(max_length=255)
    nombre = models.CharField(max_length=255)
    direccion = models.CharField(max_length=255)
    tipodocumento = models.PositiveSmallIntegerField(choices = TIPO_DOCUMENTO)
    documento = models.IntegerField()
    cuilcuit = models.CharField(max_length=255)
    fechanacimiento = models.DateField()
    edad = models.IntegerField()
    nacionalidad = models.CharField(max_length=255)
    localidad = models.ForeignKey(Localidad, blank=True, null=True)
    email = models.CharField('e-mail',max_length=255)
    fax = models.CharField(max_length=255)
    interno = models.CharField(max_length=255)
    red = models.CharField(max_length=255)
    telefono = models.CharField(max_length=255)
    situacionlaboral = models.ForeignKey("Situacionlaboral")
    fecha_creacion = models.DateTimeField(default = timezone.now())
    
    class Meta:
        verbose_name_plural = "Personas"

    def __unicode__(self):
        return u'%s %s tiene %s años' % (self.nombre, self.apellido, self.edad)

# ---------------------- #
class Programa(models.Model):    
    descripcion = models.CharField(max_length=255)
    direccion = models.CharField(max_length=255)
    mision = models.CharField(max_length=255)
    nombre = models.CharField(max_length=255)
    #contacto = models.ForeignKey("Contacto", blank=True, null=True)
    #equipotrabajo = models.ForeignKey("Equipotrabajo", blank=True, null=True)
    fondos = models.ForeignKey("Fondo", blank=True, null=True)
    instrumentolegal = models.ForeignKey("Instrumentolegal", blank=True, null=True)
    dependencia = models.ForeignKey("Dependencia", blank=True, null=True)
    email = models.CharField('e-mail',max_length=255)
    fax = models.CharField(max_length=255)
    interno = models.CharField(max_length=255)
    red = models.CharField(max_length=255)
    telefono = models.CharField(max_length=255)
    destinatario = models.ForeignKey("Destinatario")
    fecha_creacion = models.DateTimeField(default = timezone.now())
    
    class Meta:
        verbose_name_plural = "Programas"

    def __unicode__(self):
        return u'%s' % (self.descripcion)

# ---------------------- #
class Rol(models.Model):
    nombre = models.CharField(max_length=255)  
    persona = models.ForeignKey("Persona")  
    fecha_creacion = models.DateTimeField(default = timezone.now())
    class Meta:
        verbose_name_plural = "Roles"

    def __unicode__(self):
        return u'%s' % (self.nombre)

# ---------------------- #
class Responsable(Rol):    
    
    class Meta:
        verbose_name_plural = "Responsables"

    def __unicode__(self):
        return u'%s' % (self.nombre)

# ---------------------- #
class Agente(Rol):    
    
    class Meta:
        verbose_name_plural = "Agentes"

    def __unicode__(self):
        return u'%s' % (self.nombre)

# ---------------------- #
class Situacionlaboral(models.Model):    
    codigocargo = models.IntegerField('codigo de cargo')
    descripcion = models.CharField(max_length=255)
    fechaingreso = models.DateField('fecha de ingreso')
    tipocargo = models.CharField('tipo de cargo',max_length=1)
    fecha_creacion = models.DateTimeField(default = timezone.now())
    
    class Meta:
        verbose_name_plural = "Situaciones Laborales"

    def __unicode__(self):
        return u'%s' % (self.descripcion)

# ---------------------- #
class Tarea(models.Model):    
    descripcion = models.CharField(max_length=255)
    fechafin = models.DateField('fecha de finalizacion')
    fechainicio = models.DateField('fecha de inicio')
    nombre = models.CharField(max_length=255)
    prioridad = models.IntegerField()
    accion = models.ForeignKey(Accion, blank=True, null=True)
    rol = models.ForeignKey(Rol, blank=True, null=True)
    fecha_creacion = models.DateTimeField(default = timezone.now())
    
    class Meta:
        verbose_name_plural = "Tareas"

    def __unicode__(self):
        return u'%s' % (self.descripcion)