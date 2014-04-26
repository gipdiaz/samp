# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Accion'
        db.create_table(u'accion', (
            ('id', self.gf('django.db.models.fields.BigIntegerField')(primary_key=True)),
            ('descripcion', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('fechafin', self.gf('django.db.models.fields.DateField')()),
            ('fechainicio', self.gf('django.db.models.fields.DateField')()),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('programa', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['sampapp.Programa'])),
        ))
        db.send_create_signal(u'sampapp', ['Accion'])

        # Adding model 'Autorizacion'
        db.create_table(u'autorizacion', (
            ('id', self.gf('django.db.models.fields.BigIntegerField')(primary_key=True)),
            ('descripcion', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('accion', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['sampapp.Accion'], null=True, blank=True)),
        ))
        db.send_create_signal(u'sampapp', ['Autorizacion'])

        # Adding model 'Contacto'
        db.create_table(u'contacto', (
            ('id', self.gf('django.db.models.fields.BigIntegerField')(primary_key=True)),
            ('email', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('fax', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('interno', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('red', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('telefono', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal(u'sampapp', ['Contacto'])

        # Adding model 'Dependencia'
        db.create_table(u'dependencia', (
            ('id', self.gf('django.db.models.fields.BigIntegerField')(primary_key=True)),
            ('descripcion', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('autorizacion', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['sampapp.Autorizacion'], null=True, blank=True)),
            ('programa', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['sampapp.Programa'], null=True, blank=True)),
        ))
        db.send_create_signal(u'sampapp', ['Dependencia'])

        # Adding model 'Destinatario'
        db.create_table(u'destinatario', (
            ('id', self.gf('django.db.models.fields.BigIntegerField')(primary_key=True)),
            ('descripcion', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('accion', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['sampapp.Accion'], null=True, blank=True)),
        ))
        db.send_create_signal(u'sampapp', ['Destinatario'])

        # Adding model 'Equipotrabajo'
        db.create_table(u'equipotrabajo', (
            ('id', self.gf('django.db.models.fields.BigIntegerField')(primary_key=True)),
            ('descripcion', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('fechacreacion', self.gf('django.db.models.fields.DateField')()),
        ))
        db.send_create_signal(u'sampapp', ['Equipotrabajo'])

        # Adding model 'Escuela'
        db.create_table(u'escuela', (
            ('id', self.gf('django.db.models.fields.BigIntegerField')(primary_key=True)),
            ('ambito', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('anexo', self.gf('django.db.models.fields.IntegerField')()),
            ('codjurisdiccional', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('cue', self.gf('django.db.models.fields.IntegerField')()),
            ('dependencia', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('direccion', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('sector', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal(u'sampapp', ['Escuela'])

        # Adding model 'Fondos'
        db.create_table(u'fondos', (
            ('id', self.gf('django.db.models.fields.BigIntegerField')(primary_key=True)),
            ('monto', self.gf('django.db.models.fields.TextField')()),
            ('tipofinanc', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal(u'sampapp', ['Fondos'])

        # Adding model 'Instrumentolegal'
        db.create_table(u'instrumentolegal', (
            ('id', self.gf('django.db.models.fields.BigIntegerField')(primary_key=True)),
            ('descripcion', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('fecha', self.gf('django.db.models.fields.DateField')()),
            ('tipodocleg', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal(u'sampapp', ['Instrumentolegal'])

        # Adding model 'Localidad'
        db.create_table(u'localidad', (
            ('id', self.gf('django.db.models.fields.BigIntegerField')(primary_key=True)),
            ('codigopostal', self.gf('django.db.models.fields.IntegerField')()),
            ('departamento', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('region', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('accion', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['sampapp.Accion'], null=True, blank=True)),
            ('escuela', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['sampapp.Escuela'], null=True, blank=True)),
        ))
        db.send_create_signal(u'sampapp', ['Localidad'])

        # Adding model 'Nivel'
        db.create_table(u'nivel', (
            ('id', self.gf('django.db.models.fields.BigIntegerField')(primary_key=True)),
            ('codigonivel', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('descripcion', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('escuela', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['sampapp.Escuela'], null=True, blank=True)),
        ))
        db.send_create_signal(u'sampapp', ['Nivel'])

        # Adding model 'Persona'
        db.create_table(u'persona', (
            ('id', self.gf('django.db.models.fields.BigIntegerField')(primary_key=True)),
            ('apellido', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('direccion', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('dni', self.gf('django.db.models.fields.IntegerField')()),
            ('edad', self.gf('django.db.models.fields.IntegerField')()),
            ('nacionalidad', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('contacto', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['sampapp.Contacto'], null=True, blank=True)),
            ('localidad', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['sampapp.Localidad'], null=True, blank=True)),
        ))
        db.send_create_signal(u'sampapp', ['Persona'])

        # Adding model 'Programa'
        db.create_table(u'programa', (
            ('id', self.gf('django.db.models.fields.BigIntegerField')(primary_key=True)),
            ('descripcion', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('direccion', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('fechacreacion', self.gf('django.db.models.fields.DateField')()),
            ('mision', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('contacto', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['sampapp.Contacto'], null=True, blank=True)),
            ('equipotrabajo', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['sampapp.Equipotrabajo'], null=True, blank=True)),
            ('fondos', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['sampapp.Fondos'], null=True, blank=True)),
            ('instrumentolegal', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['sampapp.Instrumentolegal'], null=True, blank=True)),
        ))
        db.send_create_signal(u'sampapp', ['Programa'])

        # Adding model 'ProgramaAccion'
        db.create_table(u'programa_accion', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('programa', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['sampapp.Programa'])),
            ('accion', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['sampapp.Accion'], unique=True)),
        ))
        db.send_create_signal(u'sampapp', ['ProgramaAccion'])

        # Adding model 'Rol'
        db.create_table(u'rol', (
            ('dtype', self.gf('django.db.models.fields.CharField')(max_length=31)),
            ('id', self.gf('django.db.models.fields.BigIntegerField')(primary_key=True)),
            ('idresponsable', self.gf('django.db.models.fields.IntegerField')()),
            ('idagente', self.gf('django.db.models.fields.IntegerField')()),
            ('persona', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['sampapp.Persona'], null=True, blank=True)),
            ('programa', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['sampapp.Programa'], null=True, blank=True)),
        ))
        db.send_create_signal(u'sampapp', ['Rol'])

        # Adding model 'Situacionlaboral'
        db.create_table(u'situacionlaboral', (
            ('id', self.gf('django.db.models.fields.BigIntegerField')(primary_key=True)),
            ('codigocargo', self.gf('django.db.models.fields.IntegerField')()),
            ('descripcion', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('fechaingreso', self.gf('django.db.models.fields.DateField')()),
            ('tipocargo', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('persona', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['sampapp.Persona'], null=True, blank=True)),
        ))
        db.send_create_signal(u'sampapp', ['Situacionlaboral'])

        # Adding model 'Tarea'
        db.create_table(u'tarea', (
            ('id', self.gf('django.db.models.fields.BigIntegerField')(primary_key=True)),
            ('descripcion', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('fechafin', self.gf('django.db.models.fields.DateField')()),
            ('fechainicio', self.gf('django.db.models.fields.DateField')()),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('prioridad', self.gf('django.db.models.fields.IntegerField')()),
            ('accion', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['sampapp.Accion'], null=True, blank=True)),
            ('rol', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['sampapp.Rol'], null=True, blank=True)),
        ))
        db.send_create_signal(u'sampapp', ['Tarea'])


    def backwards(self, orm):
        # Deleting model 'Accion'
        db.delete_table(u'accion')

        # Deleting model 'Autorizacion'
        db.delete_table(u'autorizacion')

        # Deleting model 'Contacto'
        db.delete_table(u'contacto')

        # Deleting model 'Dependencia'
        db.delete_table(u'dependencia')

        # Deleting model 'Destinatario'
        db.delete_table(u'destinatario')

        # Deleting model 'Equipotrabajo'
        db.delete_table(u'equipotrabajo')

        # Deleting model 'Escuela'
        db.delete_table(u'escuela')

        # Deleting model 'Fondos'
        db.delete_table(u'fondos')

        # Deleting model 'Instrumentolegal'
        db.delete_table(u'instrumentolegal')

        # Deleting model 'Localidad'
        db.delete_table(u'localidad')

        # Deleting model 'Nivel'
        db.delete_table(u'nivel')

        # Deleting model 'Persona'
        db.delete_table(u'persona')

        # Deleting model 'Programa'
        db.delete_table(u'programa')

        # Deleting model 'ProgramaAccion'
        db.delete_table(u'programa_accion')

        # Deleting model 'Rol'
        db.delete_table(u'rol')

        # Deleting model 'Situacionlaboral'
        db.delete_table(u'situacionlaboral')

        # Deleting model 'Tarea'
        db.delete_table(u'tarea')


    models = {
        u'sampapp.accion': {
            'Meta': {'object_name': 'Accion', 'db_table': "u'accion'"},
            'descripcion': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'fechafin': ('django.db.models.fields.DateField', [], {}),
            'fechainicio': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.BigIntegerField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'programa': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sampapp.Programa']"})
        },
        u'sampapp.autorizacion': {
            'Meta': {'object_name': 'Autorizacion', 'db_table': "u'autorizacion'"},
            'accion': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sampapp.Accion']", 'null': 'True', 'blank': 'True'}),
            'descripcion': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'id': ('django.db.models.fields.BigIntegerField', [], {'primary_key': 'True'})
        },
        u'sampapp.contacto': {
            'Meta': {'object_name': 'Contacto', 'db_table': "u'contacto'"},
            'email': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'fax': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'id': ('django.db.models.fields.BigIntegerField', [], {'primary_key': 'True'}),
            'interno': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'red': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'telefono': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'sampapp.dependencia': {
            'Meta': {'object_name': 'Dependencia', 'db_table': "u'dependencia'"},
            'autorizacion': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sampapp.Autorizacion']", 'null': 'True', 'blank': 'True'}),
            'descripcion': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'id': ('django.db.models.fields.BigIntegerField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'programa': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sampapp.Programa']", 'null': 'True', 'blank': 'True'})
        },
        u'sampapp.destinatario': {
            'Meta': {'object_name': 'Destinatario', 'db_table': "u'destinatario'"},
            'accion': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sampapp.Accion']", 'null': 'True', 'blank': 'True'}),
            'descripcion': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'id': ('django.db.models.fields.BigIntegerField', [], {'primary_key': 'True'})
        },
        u'sampapp.equipotrabajo': {
            'Meta': {'object_name': 'Equipotrabajo', 'db_table': "u'equipotrabajo'"},
            'descripcion': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'fechacreacion': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.BigIntegerField', [], {'primary_key': 'True'})
        },
        u'sampapp.escuela': {
            'Meta': {'object_name': 'Escuela', 'db_table': "u'escuela'"},
            'ambito': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'anexo': ('django.db.models.fields.IntegerField', [], {}),
            'codjurisdiccional': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'cue': ('django.db.models.fields.IntegerField', [], {}),
            'dependencia': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'direccion': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'id': ('django.db.models.fields.BigIntegerField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'sector': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'sampapp.fondos': {
            'Meta': {'object_name': 'Fondos', 'db_table': "u'fondos'"},
            'id': ('django.db.models.fields.BigIntegerField', [], {'primary_key': 'True'}),
            'monto': ('django.db.models.fields.TextField', [], {}),
            'tipofinanc': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'sampapp.instrumentolegal': {
            'Meta': {'object_name': 'Instrumentolegal', 'db_table': "u'instrumentolegal'"},
            'descripcion': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'fecha': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.BigIntegerField', [], {'primary_key': 'True'}),
            'tipodocleg': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'sampapp.localidad': {
            'Meta': {'object_name': 'Localidad', 'db_table': "u'localidad'"},
            'accion': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sampapp.Accion']", 'null': 'True', 'blank': 'True'}),
            'codigopostal': ('django.db.models.fields.IntegerField', [], {}),
            'departamento': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'escuela': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sampapp.Escuela']", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.BigIntegerField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'region': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'sampapp.nivel': {
            'Meta': {'object_name': 'Nivel', 'db_table': "u'nivel'"},
            'codigonivel': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'descripcion': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'escuela': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sampapp.Escuela']", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.BigIntegerField', [], {'primary_key': 'True'})
        },
        u'sampapp.persona': {
            'Meta': {'object_name': 'Persona', 'db_table': "u'persona'"},
            'apellido': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'contacto': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sampapp.Contacto']", 'null': 'True', 'blank': 'True'}),
            'direccion': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'dni': ('django.db.models.fields.IntegerField', [], {}),
            'edad': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.BigIntegerField', [], {'primary_key': 'True'}),
            'localidad': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sampapp.Localidad']", 'null': 'True', 'blank': 'True'}),
            'nacionalidad': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'sampapp.programa': {
            'Meta': {'object_name': 'Programa', 'db_table': "u'programa'"},
            'contacto': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sampapp.Contacto']", 'null': 'True', 'blank': 'True'}),
            'descripcion': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'direccion': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'equipotrabajo': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sampapp.Equipotrabajo']", 'null': 'True', 'blank': 'True'}),
            'fechacreacion': ('django.db.models.fields.DateField', [], {}),
            'fondos': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sampapp.Fondos']", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.BigIntegerField', [], {'primary_key': 'True'}),
            'instrumentolegal': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sampapp.Instrumentolegal']", 'null': 'True', 'blank': 'True'}),
            'mision': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'sampapp.programaaccion': {
            'Meta': {'object_name': 'ProgramaAccion', 'db_table': "u'programa_accion'"},
            'accion': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sampapp.Accion']", 'unique': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'programa': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sampapp.Programa']"})
        },
        u'sampapp.rol': {
            'Meta': {'object_name': 'Rol', 'db_table': "u'rol'"},
            'dtype': ('django.db.models.fields.CharField', [], {'max_length': '31'}),
            'id': ('django.db.models.fields.BigIntegerField', [], {'primary_key': 'True'}),
            'idagente': ('django.db.models.fields.IntegerField', [], {}),
            'idresponsable': ('django.db.models.fields.IntegerField', [], {}),
            'persona': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sampapp.Persona']", 'null': 'True', 'blank': 'True'}),
            'programa': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sampapp.Programa']", 'null': 'True', 'blank': 'True'})
        },
        u'sampapp.situacionlaboral': {
            'Meta': {'object_name': 'Situacionlaboral', 'db_table': "u'situacionlaboral'"},
            'codigocargo': ('django.db.models.fields.IntegerField', [], {}),
            'descripcion': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'fechaingreso': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.BigIntegerField', [], {'primary_key': 'True'}),
            'persona': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sampapp.Persona']", 'null': 'True', 'blank': 'True'}),
            'tipocargo': ('django.db.models.fields.CharField', [], {'max_length': '1'})
        },
        u'sampapp.tarea': {
            'Meta': {'object_name': 'Tarea', 'db_table': "u'tarea'"},
            'accion': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sampapp.Accion']", 'null': 'True', 'blank': 'True'}),
            'descripcion': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'fechafin': ('django.db.models.fields.DateField', [], {}),
            'fechainicio': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.BigIntegerField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'prioridad': ('django.db.models.fields.IntegerField', [], {}),
            'rol': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sampapp.Rol']", 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['sampapp']