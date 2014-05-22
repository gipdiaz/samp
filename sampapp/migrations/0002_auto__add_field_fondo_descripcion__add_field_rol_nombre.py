# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Fondo.descripcion'
        db.add_column(u'sampapp_fondo', 'descripcion',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=255),
                      keep_default=False)

        # Adding field 'Rol.nombre'
        db.add_column(u'sampapp_rol', 'nombre',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=255),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Fondo.descripcion'
        db.delete_column(u'sampapp_fondo', 'descripcion')

        # Deleting field 'Rol.nombre'
        db.delete_column(u'sampapp_rol', 'nombre')


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
            'descripcion': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
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
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
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