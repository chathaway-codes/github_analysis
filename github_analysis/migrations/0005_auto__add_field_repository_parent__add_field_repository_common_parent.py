# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Repository.parent'
        db.add_column(u'github_analysis_repository', 'parent',
                      self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='children', null=True, to=orm['github_analysis.Repository']),
                      keep_default=False)

        # Adding field 'Repository.common_parent'
        db.add_column(u'github_analysis_repository', 'common_parent',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Repository.parent'
        db.delete_column(u'github_analysis_repository', 'parent_id')

        # Deleting field 'Repository.common_parent'
        db.delete_column(u'github_analysis_repository', 'common_parent')


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
            'common_parent': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'fork': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'full_name': ('django.db.models.fields.CharField', [], {'max_length': '1024'}),
            'html_url': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '1024'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['github_analysis.GithubUser']"}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'children'", 'null': 'True', 'to': u"orm['github_analysis.Repository']"}),
            'private': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['github_analysis']