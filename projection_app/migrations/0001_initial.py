# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'State'
        db.create_table(u'projection_app_state', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('state_name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=100)),
            ('sub_region', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('geometry', self.gf('django.contrib.gis.db.models.fields.MultiPolygonField')(db_column='geom')),
        ))
        db.send_create_signal('projection_app', ['State'])

        # Adding model 'Occupation'
        db.create_table(u'projection_app_occupation', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('area_name', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['projection_app.State'], to_field='state_name', null=True, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('base', self.gf('django.db.models.fields.IntegerField')()),
            ('proj', self.gf('django.db.models.fields.IntegerField')()),
            ('change', self.gf('django.db.models.fields.IntegerField')()),
            ('percentchange', self.gf('django.db.models.fields.IntegerField')()),
            ('avgannualopenings', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('projection_app', ['Occupation'])


    def backwards(self, orm):
        # Deleting model 'State'
        db.delete_table(u'projection_app_state')

        # Deleting model 'Occupation'
        db.delete_table(u'projection_app_occupation')


    models = {
        'projection_app.occupation': {
            'Meta': {'object_name': 'Occupation'},
            'area_name': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['projection_app.State']", 'to_field': "'state_name'", 'null': 'True', 'blank': 'True'}),
            'avgannualopenings': ('django.db.models.fields.IntegerField', [], {}),
            'base': ('django.db.models.fields.IntegerField', [], {}),
            'change': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'percentchange': ('django.db.models.fields.IntegerField', [], {}),
            'proj': ('django.db.models.fields.IntegerField', [], {})
        },
        'projection_app.state': {
            'Meta': {'object_name': 'State'},
            'geometry': ('django.contrib.gis.db.models.fields.MultiPolygonField', [], {'db_column': "'geom'"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'state_name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'}),
            'sub_region': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['projection_app']