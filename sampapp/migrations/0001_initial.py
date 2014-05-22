# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Accion'
        db.create_table(u'sampapp_accion', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('autorizacion', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['sampapp.Autorizacion'], null=True, blank=True)),
            ('descripcion', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('fechainicio', self.gf('django.db.models.fields.DateField')()),
            ('fechafin', self.gf('django.db.models.fields.DateField')()),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('programa', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['sampapp.Programa'])),
            ('destinatario', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['sampapp.Destinatario'])),
            ('fecha_creacion', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2014, 5, 22, 0, 0))),
        ))
        db.send_create_signal(u'sampapp', ['Accion'])

        # Adding model 'Autorizacion'
        db.create_table(u'sampapp_autorizacion', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('descripcion', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('estado', self.gf('django.db.models.fields.BooleanField')()),
            ('dependencia', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['sampapp.Dependencia'])),
            ('fecha_creacion', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2014, 5, 22, 0, 0))),
        ))
        db.send_create_signal(u'sampapp', ['Autorizacion'])

        # Adding model 'Dependencia'
        db.create_table(u'sampapp_dependencia', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('descripcion', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('dependencia', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='depende', null=True, to=orm['sampapp.Dependencia'])),
            ('responsable', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['sampapp.Responsable'], null=True, blank=True)),
            ('fecha_creacion', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2014, 5, 22, 0, 0))),
        ))
        db.send_create_signal(u'sampapp', ['Dependencia'])

        # Adding model 'Destinatario'
        db.create_table(u'sampapp_destinatario', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('descripcion', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('fecha_creacion', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2014, 5, 22, 0, 0))),
        ))
        db.send_create_signal(u'sampapp', ['Destinatario'])

        # Adding model 'Escuela'
        db.create_table(u'sampapp_escuela', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('tipo_ambito', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
            ('ambito', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('anexo', self.gf('django.db.models.fields.IntegerField')()),
            ('codjurisdiccional', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('cue', self.gf('django.db.models.fields.IntegerField')()),
            ('dependencia', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
            ('direccion', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('estado', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('sector', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
            ('nivel', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
            ('orientacion', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
            ('localidad', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['sampapp.Localidad'], null=True, blank=True)),
            ('fecha_creacion', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2014, 5, 22, 0, 0))),
        ))
        db.send_create_signal(u'sampapp', ['Escuela'])

        # Adding model 'Fondo'
        db.create_table(u'sampapp_fondo', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('monto', self.gf('django.db.models.fields.FloatField')()),
            ('tipofinanciacion', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
            ('fecha_creacion', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2014, 5, 22, 0, 0))),
        ))
        db.send_create_signal(u'sampapp', ['Fondo'])

        # Adding model 'Instrumentolegal'
        db.create_table(u'sampapp_instrumentolegal', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('descripcion', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('tipodocleg', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('fecha_creacion', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2014, 5, 22, 0, 0))),
        ))
        db.send_create_signal(u'sampapp', ['Instrumentolegal'])

        # Adding model 'Localidad'
        db.create_table(u'sampapp_localidad', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('codigopostal', self.gf('django.db.models.fields.IntegerField')()),
            ('departamento', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('region', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
            ('accion', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['sampapp.Accion'], null=True, blank=True)),
            ('fecha_creacion', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2014, 5, 22, 0, 0))),
        ))
        db.send_create_signal(u'sampapp', ['Localidad'])

        # Adding model 'Persona'
        db.create_table(u'sampapp_persona', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('apellido', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('direccion', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('tipodocumento', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
            ('documento', self.gf('django.db.models.fields.IntegerField')()),
            ('cuilcuit', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('fechanacimiento', self.gf('django.db.models.fields.DateField')()),
            ('edad', self.gf('django.db.models.fields.IntegerField')()),
            ('nacionalidad', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('localidad', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['sampapp.Localidad'], null=True, blank=True)),
            ('email', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('fax', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('interno', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('red', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('telefono', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('situacionlaboral', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['sampapp.Situacionlaboral'])),
            ('fecha_creacion', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2014, 5, 22, 0, 0))),
        ))
        db.send_create_signal(u'sampapp', ['Persona'])

        # Adding model 'Programa'
        db.create_table(u'sampapp_programa', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('descripcion', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('direccion', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('mision', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('fondos', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['sampapp.Fondo'], null=True, blank=True)),
            ('instrumentolegal', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['sampapp.Instrumentolegal'], null=True, blank=True)),
            ('dependencia', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['sampapp.Dependencia'], null=True, blank=True)),
            ('email', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('fax', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('interno', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('red', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('telefono', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('destinatario', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['sampapp.Destinatario'])),
            ('fecha_creacion', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2014, 5, 22, 0, 0))),
        ))
        db.send_create_signal(u'sampapp', ['Programa'])

        # Adding model 'Rol'
        db.create_table(u'sampapp_rol', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('persona', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['sampapp.Persona'])),
            ('fecha_creacion', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2014, 5, 22, 0, 0))),
        ))
        db.send_create_signal(u'sampapp', ['Rol'])

        # Adding model 'Responsable'
        db.create_table(u'sampapp_responsable', (
            (u'rol_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['sampapp.Rol'], unique=True, primary_key=True)),
        ))
        db.send_create_signal(u'sampapp', ['Responsable'])

        # Adding model 'Agente'
        db.create_table(u'sampapp_agente', (
            (u'rol_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['sampapp.Rol'], unique=True, primary_key=True)),
        ))
        db.send_create_signal(u'sampapp', ['Agente'])

        # Adding model 'Situacionlaboral'
        db.create_table(u'sampapp_situacionlaboral', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('codigocargo', self.gf('django.db.models.fields.IntegerField')()),
            ('descripcion', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('fechaingreso', self.gf('django.db.models.fields.DateField')()),
            ('tipocargo', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('fecha_creacion', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2014, 5, 22, 0, 0))),
        ))
        db.send_create_signal(u'sampapp', ['Situacionlaboral'])

        # Adding model 'Tarea'
        db.create_table(u'sampapp_tarea', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('descripcion', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('fechafin', self.gf('django.db.models.fields.DateField')()),
            ('fechainicio', self.gf('django.db.models.fields.DateField')()),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('prioridad', self.gf('django.db.models.fields.IntegerField')()),
            ('accion', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['sampapp.Accion'], null=True, blank=True)),
            ('rol', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['sampapp.Rol'], null=True, blank=True)),
            ('fecha_creacion', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2014, 5, 22, 0, 0))),
        ))
        db.send_create_signal(u'sampapp', ['Tarea'])


    def backwards(self, orm):
        # Deleting model 'Accion'
        db.delete_table(u'sampapp_accion')

        # Deleting model 'Autorizacion'
        db.delete_table(u'sampapp_autorizacion')

        # Deleting model 'Dependencia'
        db.delete_table(u'sampapp_dependencia')

        # Deleting model 'Destinatario'
        db.delete_table(u'sampapp_destinatario')

        # Deleting model 'Escuela'
        db.delete_table(u'sampapp_escuela')

        # Deleting model 'Fondo'
        db.delete_table(u'sampapp_fondo')

        # Deleting model 'Instrumentolegal'
        db.delete_table(u'sampapp_instrumentolegal')

        # Deleting model 'Localidad'
        db.delete_table(u'sampapp_localidad')

        # Deleting model 'Persona'
        db.delete_table(u'sampapp_persona')

        # Deleting model 'Programa'
        db.delete_table(u'sampapp_programa')

        # Deleting model 'Rol'
        db.delete_table(u'sampapp_rol')

        # Deleting model 'Responsable'
        db.delete_table(u'sampapp_responsable')

        # Deleting model 'Agente'
        db.delete_table(u'sampapp_agente')

        # Deleting model 'Situacionlaboral'
        db.delete_table(u'sampapp_situacionlaboral')

        # Deleting model 'Tarea'
        db.delete_table(u'sampapp_tarea')


    models = {
        u'sampapp.accion': {
            'Meta': {'object_name': 'Accion'},
            'autorizacion': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sampapp.Autorizacion']", 'null': 'True', 'blank': 'True'}),
            'descripcion': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'destinatario': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sampapp.Destinatario']"}),
            'fecha_creacion': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 5, 22, 0, 0)'}),
            'fechafin': ('django.db.models.fields.DateField', [], {}),
            'fechainicio': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'programa': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sampapp.Programa']"})
        },
        u'sampapp.agente': {
            'Meta': {'object_name': 'Agente', '_ormbases': [u'sampapp.Rol']},
            u'rol_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['sampapp.Rol']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'sampapp.autorizacion': {
            'Meta': {'object_name': 'Autorizacion'},
            'dependencia': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sampapp.Dependencia']"}),
            'descripcion': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'estado': ('django.db.models.fields.BooleanField', [], {}),
            'fecha_creacion': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 5, 22, 0, 0)'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'sampapp.dependencia': {
            'Meta': {'object_name': 'Dependencia'},
            'dependencia': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'depende'", 'null': 'True', 'to': u"orm['sampapp.Dependencia']"}),
            'descripcion': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'fecha_creacion': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 5, 22, 0, 0)'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'responsable': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sampapp.Responsable']", 'null': 'True', 'blank': 'True'})
        },
        u'sampapp.destinatario': {
            'Meta': {'object_name': 'Destinatario'},
            'descripcion': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'fecha_creacion': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 5, 22, 0, 0)'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'sampapp.escuela': {
            'Meta': {'object_name': 'Escuela'},
            'ambito': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'anexo': ('django.db.models.fields.IntegerField', [], {}),
            'codjurisdiccional': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'cue': ('django.db.models.fields.IntegerField', [], {}),
            'dependencia': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'direccion': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'estado': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'fecha_creacion': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 5, 22, 0, 0)'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'localidad': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sampapp.Localidad']", 'null': 'True', 'blank': 'True'}),
            'nivel': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'orientacion': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'sector': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'tipo_ambito': ('django.db.models.fields.PositiveSmallIntegerField', [], {})
        },
        u'sampapp.fondo': {
            'Meta': {'object_name': 'Fondo'},
            'fecha_creacion': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 5, 22, 0, 0)'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'monto': ('django.db.models.fields.FloatField', [], {}),
            'tipofinanciacion': ('django.db.models.fields.PositiveSmallIntegerField', [], {})
        },
        u'sampapp.instrumentolegal': {
            'Meta': {'object_name': 'Instrumentolegal'},
            'descripcion': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'fecha_creacion': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 5, 22, 0, 0)'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'tipodocleg': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'sampapp.localidad': {
            'Meta': {'object_name': 'Localidad'},
            'accion': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sampapp.Accion']", 'null': 'True', 'blank': 'True'}),
            'codigopostal': ('django.db.models.fields.IntegerField', [], {}),
            'departamento': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'fecha_creacion': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 5, 22, 0, 0)'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'region': ('django.db.models.fields.PositiveSmallIntegerField', [], {})
        },
        u'sampapp.persona': {
            'Meta': {'object_name': 'Persona'},
            'apellido': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'cuilcuit': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'direccion': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'documento': ('django.db.models.fields.IntegerField', [], {}),
            'edad': ('django.db.models.fields.IntegerField', [], {}),
            'email': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'fax': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'fecha_creacion': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 5, 22, 0, 0)'}),
            'fechanacimiento': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'interno': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'localidad': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sampapp.Localidad']", 'null': 'True', 'blank': 'True'}),
            'nacionalidad': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'red': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'situacionlaboral': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sampapp.Situacionlaboral']"}),
            'telefono': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'tipodocumento': ('django.db.models.fields.PositiveSmallIntegerField', [], {})
        },
        u'sampapp.programa': {
            'Meta': {'object_name': 'Programa'},
            'dependencia': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sampapp.Dependencia']", 'null': 'True', 'blank': 'True'}),
            'descripcion': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'destinatario': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sampapp.Destinatario']"}),
            'direccion': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'email': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'fax': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'fecha_creacion': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 5, 22, 0, 0)'}),
            'fondos': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sampapp.Fondo']", 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'instrumentolegal': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sampapp.Instrumentolegal']", 'null': 'True', 'blank': 'True'}),
            'interno': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'mision': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'red': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'telefono': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'sampapp.responsable': {
            'Meta': {'object_name': 'Responsable', '_ormbases': [u'sampapp.Rol']},
            u'rol_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['sampapp.Rol']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'sampapp.rol': {
            'Meta': {'object_name': 'Rol'},
            'fecha_creacion': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 5, 22, 0, 0)'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'persona': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sampapp.Persona']"})
        },
        u'sampapp.situacionlaboral': {
            'Meta': {'object_name': 'Situacionlaboral'},
            'codigocargo': ('django.db.models.fields.IntegerField', [], {}),
            'descripcion': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'fecha_creacion': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 5, 22, 0, 0)'}),
            'fechaingreso': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'tipocargo': ('django.db.models.fields.CharField', [], {'max_length': '1'})
        },
        u'sampapp.tarea': {
            'Meta': {'object_name': 'Tarea'},
            'accion': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sampapp.Accion']", 'null': 'True', 'blank': 'True'}),
            'descripcion': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'fecha_creacion': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 5, 22, 0, 0)'}),
            'fechafin': ('django.db.models.fields.DateField', [], {}),
            'fechainicio': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'prioridad': ('django.db.models.fields.IntegerField', [], {}),
            'rol': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sampapp.Rol']", 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['sampapp']