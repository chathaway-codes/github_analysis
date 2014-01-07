# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'GithubUser.gravatar_id'
        db.alter_column(u'github_analysis_githubuser', 'gravatar_id', self.gf('django.db.models.fields.CharField')(max_length=1024, null=True))

        # Changing field 'GithubUser.login'
        db.alter_column(u'github_analysis_githubuser', 'login', self.gf('django.db.models.fields.CharField')(max_length=1024))

        # Changing field 'Repository.description'
        db.alter_column(u'github_analysis_repository', 'description', self.gf('django.db.models.fields.CharField')(max_length=1024))

        # Changing field 'Repository.full_name'
        db.alter_column(u'github_analysis_repository', 'full_name', self.gf('django.db.models.fields.CharField')(max_length=1024))

        # Changing field 'Repository.name'
        db.alter_column(u'github_analysis_repository', 'name', self.gf('django.db.models.fields.CharField')(max_length=1024))

    def backwards(self, orm):

        # Changing field 'GithubUser.gravatar_id'
        db.alter_column(u'github_analysis_githubuser', 'gravatar_id', self.gf('django.db.models.fields.CharField')(max_length=255, null=True))

        # Changing field 'GithubUser.login'
        db.alter_column(u'github_analysis_githubuser', 'login', self.gf('django.db.models.fields.CharField')(max_length=255))

        # Changing field 'Repository.description'
        db.alter_column(u'github_analysis_repository', 'description', self.gf('django.db.models.fields.CharField')(max_length=255))

        # Changing field 'Repository.full_name'
        db.alter_column(u'github_analysis_repository', 'full_name', self.gf('django.db.models.fields.CharField')(max_length=255))

        # Changing field 'Repository.name'
        db.alter_column(u'github_analysis_repository', 'name', self.gf('django.db.models.fields.CharField')(max_length=255))

    models = {
        u'github_analysis.contribution': {
            'Meta': {'object_name': 'Contribution'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'repo': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['github_analysis.Repository']"}),
            'total_added': ('django.db.models.fields.IntegerField', [], {}),
            'total_changed': ('django.db.models.fields.IntegerField', [], {}),
            'total_contributions': ('django.db.models.fields.IntegerField', [], {}),
            'total_deleted': ('django.db.models.fields.IntegerField', [], {}),
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