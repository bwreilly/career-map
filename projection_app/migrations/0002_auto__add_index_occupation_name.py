# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding index on 'Occupation', fields ['name']
        db.create_index('careermap_occupation', ['name'])


    def backwards(self, orm):
        # Removing index on 'Occupation', fields ['name']
        db.delete_index('careermap_occupation', ['name'])


    models = {
        'projection_app.occupation': {
            'Meta': {'object_name': 'Occupation', 'db_table': "'careermap_occupation'"},
            'area_name': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['projection_app.State']", 'to_field': "'state_name'", 'null': 'True', 'blank': 'True'}),
            'avgannualopenings': ('django.db.models.fields.IntegerField', [], {}),
            'base': ('django.db.models.fields.IntegerField', [], {}),
            'change': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_index': 'True'}),
            'percentchange': ('django.db.models.fields.IntegerField', [], {}),
            'proj': ('django.db.models.fields.IntegerField', [], {})
        },
        'projection_app.state': {
            'Meta': {'object_name': 'State', 'db_table': "'careermap_state'"},
            'geometry': ('django.contrib.gis.db.models.fields.MultiPolygonField', [], {'db_column': "'geom'"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'state_name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'}),
            'sub_region': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['projection_app']