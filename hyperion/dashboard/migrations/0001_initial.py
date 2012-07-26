# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Graph'
        db.create_table('dashboard_graph', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('query', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('dashboard', ['Graph'])


    def backwards(self, orm):
        
        # Deleting model 'Graph'
        db.delete_table('dashboard_graph')


    models = {
        'dashboard.graph': {
            'Meta': {'object_name': 'Graph'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'query': ('django.db.models.fields.TextField', [], {})
        }
    }

    complete_apps = ['dashboard']
