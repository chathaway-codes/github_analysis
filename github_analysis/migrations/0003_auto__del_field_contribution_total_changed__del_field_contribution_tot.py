# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Contribution.total_changed'
        db.delete_column(u'github_analysis_contribution', 'total_changed')

        # Deleting field 'Contribution.total_added'
        db.delete_column(u'github_analysis_contribution', 'total_added')

        # Deleting field 'Contribution.total_deleted'
        db.delete_column(u'github_analysis_contribution', 'total_deleted')


    def backwards(self, orm):
        # Adding field 'Contribution.total_changed'
        db.add_column(u'github_analysis_contribution', 'total_changed',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Contribution.total_added'
        db.add_column(u'github_analysis_contribution', 'total_added',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Contribution.total_deleted'
        db.add_column(u'github_analysis_contribution', 'total_deleted',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)


    models = {
        u'github_analysis.contribution': {
            'Meta': {'object_name': 'Contribution'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'repo': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['github_analysis.Repository']"}),
            'total_contributions': ('django.db.models.fields.IntegerField', [], {}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['github_analysis.GithubUser']"})
        },
        u'github_analysis.githubuser': {
            'Meta': {'object_name': 'GithubUser'},
            'followers': ('django.db.models.fields.IntegerField', [], {}),
            'followers_url': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'following': ('django.db.models.fields.IntegerField', [], {}),
            'following_url': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'gravatar_id': ('django.db.models.fields.CharField', [], {'max_length': '1024', 'null': 'True'}),
            'html_url': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'login': ('django.db.models.fields.CharField', [], {'max_length': '1024'}),
            'organizations_url': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'repos_url': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'starred_url': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'subscriptions_url': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        },
        u'github_analysis.repository': {
            'Meta': {'object_name': 'Repository'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '1024'}),
            'fork': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'full_name': ('django.db.models.fields.CharField', [], {'max_length': '1024'}),
            'html_url': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '1024'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['github_analysis.GithubUser']"}),
            'private': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['github_analysis']