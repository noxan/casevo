# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Removing unique constraint on 'Account', fields ['identifier']
        db.delete_unique(u'accounts_account', ['identifier'])

        # Adding field 'Account.blz'
        db.add_column(u'accounts_account', 'blz',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=100),
                      keep_default=False)

        # Adding unique constraint on 'Account', fields ['number', 'blz']
        db.create_unique(u'accounts_account', ['number', 'blz'])


    def backwards(self, orm):
        # Removing unique constraint on 'Account', fields ['number', 'blz']
        db.delete_unique(u'accounts_account', ['number', 'blz'])

        # Deleting field 'Account.blz'
        db.delete_column(u'accounts_account', 'blz')

        # Adding unique constraint on 'Account', fields ['identifier']
        db.create_unique(u'accounts_account', ['identifier'])


    models = {
        u'accounts.account': {
            'Meta': {'unique_together': "[('number', 'blz')]", 'object_name': 'Account'},
            'blz': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'currency': ('django.db.models.fields.related.ForeignKey', [], {'default': '0', 'to': u"orm['currencies.Currency']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'identifier': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'number': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'currencies.currency': {
            'Meta': {'ordering': "('name',)", 'object_name': 'Currency'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'factor': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '4'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_base': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_default': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '35'}),
            'symbol': ('django.db.models.fields.CharField', [], {'max_length': '4', 'blank': 'True'})
        }
    }

    complete_apps = ['accounts']