# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        pass

    def backwards(self, orm):
        pass

    models = {
        u'sampapp.accion': {
            'Meta': {'object_name': 'Accion', 'db_table': "u'accion'", 'managed': 'False'},
            'descripcion': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'fechafin': ('django.db.models.fields.DateField', [], {}),
            'fechainicio': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.BigIntegerField', [], {'primary_key': 'True'}),
            'idaccion': ('django.db.models.fields.IntegerField', [], {}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'programa': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sampapp.Programa']"})
        },
        u'sampapp.autorizacion': {
            'Meta': {'object_name': 'Autorizacion', 'db_table': "u'autorizacion'", 'managed': 'False'},
            'accion': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sampapp.Accion']", 'null': 'True', 'blank': 'True'}),
            'descripcion': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'id': ('django.db.models.fields.BigIntegerField', [], {'primary_key': 'True'}),
            'idautorizacion': ('django.db.models.fields.IntegerField', [], {})
        },
        u'sampapp.contacto': {
            'Meta': {'object_name': 'Contacto', 'db_table': "u'contacto'", 'managed': 'False'},
            'email': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'fax': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'id': ('django.db.models.fields.BigIntegerField', [], {'primary_key': 'True'}),
            'idcontacto': ('django.db.models.fields.IntegerField', [], {}),
            'interno': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'red': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'telefono': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'sampapp.dependencia': {
            'Meta': {'object_name': 'Dependencia', 'db_table': "u'dependencia'", 'managed': 'False'},
            'autorizacion': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sampapp.Autorizacion']", 'null': 'True', 'blank': 'True'}),
            'descripcion': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'id': ('django.db.models.fields.BigIntegerField', [], {'primary_key': 'True'}),
            'iddependencia': ('django.db.models.fields.IntegerField', [], {}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'programa': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sampapp.Programa']", 'null': 'True', 'blank': 'True'})
        },
        u'sampapp.destinatario': {
            'Meta': {'object_name': 'Destinatario', 'db_table': "u'destinatario'", 'managed': 'False'},
            'accion': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sampapp.Accion']", 'null': 'True', 'blank': 'True'}),
            'descripcion': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'id': ('django.db.models.fields.BigIntegerField', [], {'primary_key': 'True'}),
            'iddestinatario': ('django.db.models.fields.IntegerField', [], {})
        },
        u'sampapp.equipotrabajo': {
            'Meta': {'object_name': 'Equipotrabajo', 'db_table': "u'equipotrabajo'", 'managed': 'False'},
            'descripcion': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'fechacreacion': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.BigIntegerField', [], {'primary_key': 'True'}),
            'idequipotrabajo': ('django.db.models.fields.IntegerField', [], {})
        },
        u'sampapp.escuela': {
            'Meta': {'object_name': 'Escuela', 'db_table': "u'escuela'", 'managed': 'False'},
            'ambito': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'anexo': ('django.db.models.fields.IntegerField', [], {}),
            'codjurisdiccional': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'cue': ('django.db.models.fields.IntegerField', [], {}),
            'dependencia': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'direccion': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'id': ('django.db.models.fields.BigIntegerField', [], {'primary_key': 'True'}),
            'idescuela': ('django.db.models.fields.IntegerField', [], {}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'sector': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'sampapp.fondos': {
            'Meta': {'object_name': 'Fondos', 'db_table': "u'fondos'", 'managed': 'False'},
            'id': ('django.db.models.fields.BigIntegerField', [], {'primary_key': 'True'}),
            'idfondo': ('django.db.models.fields.IntegerField', [], {}),
            'monto': ('django.db.models.fields.TextField', [], {}),
            'tipofinanc': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'sampapp.instrumentolegal': {
            'Meta': {'object_name': 'Instrumentolegal', 'db_table': "u'instrumentolegal'", 'managed': 'False'},
            'descripcion': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'fecha': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.BigIntegerField', [], {'primary_key': 'True'}),
            'idinstrumentolegal': ('django.db.models.fields.IntegerField', [], {}),
            'tipodocleg': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'sampapp.localidad': {
            'Meta': {'object_name': 'Localidad', 'db_table': "u'localidad'", 'managed': 'False'},
            'accion': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sampapp.Accion']", 'null': 'True', 'blank': 'True'}),
            'codigopostal': ('django.db.models.fields.IntegerField', [], {}),
            'departamento': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'escuela': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sampapp.Escuela']", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.BigIntegerField', [], {'primary_key': 'True'}),
            'idlocalidad': ('django.db.models.fields.IntegerField', [], {}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'region': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'sampapp.nivel': {
            'Meta': {'object_name': 'Nivel', 'db_table': "u'nivel'", 'managed': 'False'},
            'codigonivel': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'descripcion': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'escuela': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sampapp.Escuela']", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.BigIntegerField', [], {'primary_key': 'True'}),
            'idnivel': ('django.db.models.fields.IntegerField', [], {})
        },
        u'sampapp.persona': {
            'Meta': {'object_name': 'Persona', 'db_table': "u'persona'", 'managed': 'False'},
            'apellido': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'contacto': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sampapp.Contacto']", 'null': 'True', 'blank': 'True'}),
            'direccion': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'dni': ('django.db.models.fields.IntegerField', [], {}),
            'edad': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.BigIntegerField', [], {'primary_key': 'True'}),
            'idpersona': ('django.db.models.fields.IntegerField', [], {}),
            'localidad': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sampapp.Localidad']", 'null': 'True', 'blank': 'True'}),
            'nacionalidad': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'sampapp.programa': {
            'Meta': {'object_name': 'Programa', 'db_table': "u'programa'", 'managed': 'False'},
            'contacto': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sampapp.Contacto']", 'null': 'True', 'blank': 'True'}),
            'descripcion': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'direccion': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'equipotrabajo': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sampapp.Equipotrabajo']", 'null': 'True', 'blank': 'True'}),
            'fechacreacion': ('django.db.models.fields.DateField', [], {}),
            'fondos': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sampapp.Fondos']", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.BigIntegerField', [], {'primary_key': 'True'}),
            'idprograma': ('django.db.models.fields.IntegerField', [], {}),
            'instrumentolegal': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sampapp.Instrumentolegal']", 'null': 'True', 'blank': 'True'}),
            'mision': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'sampapp.programaaccion': {
            'Meta': {'object_name': 'ProgramaAccion', 'db_table': "u'programa_accion'", 'managed': 'False'},
            'accion': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sampapp.Accion']", 'unique': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'programa': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sampapp.Programa']"})
        },
        u'sampapp.rol': {
            'Meta': {'object_name': 'Rol', 'db_table': "u'rol'", 'managed': 'False'},
            'dtype': ('django.db.models.fields.CharField', [], {'max_length': '31'}),
            'id': ('django.db.models.fields.BigIntegerField', [], {'primary_key': 'True'}),
            'idagente': ('django.db.models.fields.IntegerField', [], {}),
            'idresponsable': ('django.db.models.fields.IntegerField', [], {}),
            'idrol': ('django.db.models.fields.IntegerField', [], {}),
            'persona': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sampapp.Persona']", 'null': 'True', 'blank': 'True'}),
            'programa': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sampapp.Programa']", 'null': 'True', 'blank': 'True'})
        },
        u'sampapp.situacionlaboral': {
            'Meta': {'object_name': 'Situacionlaboral', 'db_table': "u'situacionlaboral'", 'managed': 'False'},
            'codigocargo': ('django.db.models.fields.IntegerField', [], {}),
            'descripcion': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'fechaingreso': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.BigIntegerField', [], {'primary_key': 'True'}),
            'idsituacionlaboral': ('django.db.models.fields.IntegerField', [], {}),
            'persona': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sampapp.Persona']", 'null': 'True', 'blank': 'True'}),
            'tipocargo': ('django.db.models.fields.CharField', [], {'max_length': '1'})
        },
        u'sampapp.tarea': {
            'Meta': {'object_name': 'Tarea', 'db_table': "u'tarea'", 'managed': 'False'},
            'accion': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sampapp.Accion']", 'null': 'True', 'blank': 'True'}),
            'descripcion': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'fechafin': ('django.db.models.fields.DateField', [], {}),
            'fechainicio': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.BigIntegerField', [], {'primary_key': 'True'}),
            'idtarea': ('django.db.models.fields.IntegerField', [], {}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'prioridad': ('django.db.models.fields.IntegerField', [], {}),
            'rol': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sampapp.Rol']", 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['sampapp']