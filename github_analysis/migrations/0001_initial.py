# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Repository'
        db.create_table(u'github_analysis_repository', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('owner', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['github_analysis.GithubUser'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('full_name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('private', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('fork', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('html_url', self.gf('django.db.models.fields.URLField')(max_length=200)),
        ))
        db.send_create_signal(u'github_analysis', ['Repository'])

        # Adding model 'GithubUser'
        db.create_table(u'github_analysis_githubuser', (
            ('login', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('gravatar_id', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('html_url', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('followers_url', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('following_url', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('starred_url', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('subscriptions_url', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('organizations_url', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('repos_url', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('followers', self.gf('django.db.models.fields.IntegerField')()),
            ('following', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'github_analysis', ['GithubUser'])

        # Adding model 'Contribution'
        db.create_table(u'github_analysis_contribution', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['github_analysis.GithubUser'])),
            ('repo', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['github_analysis.Repository'])),
            ('total_contributions', self.gf('django.db.models.fields.IntegerField')()),
            ('total_added', self.gf('django.db.models.fields.IntegerField')()),
            ('total_deleted', self.gf('django.db.models.fields.IntegerField')()),
            ('total_changed', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'github_analysis', ['Contribution'])


    def backwards(self, orm):
        # Deleting model 'Repository'
        db.delete_table(u'github_analysis_repository')

        # Deleting model 'GithubUser'
        db.delete_table(u'github_analysis_githubuser')

        # Deleting model 'Contribution'
        db.delete_table(u'github_analysis_contribution')


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
            'gravatar_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'html_url': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'login': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'organizations_url': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'repos_url': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'starred_url': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'subscriptions_url': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        },
        u'github_analysis.repository': {
            'Meta': {'object_name': 'Repository'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'fork': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'full_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'html_url': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['github_analysis.GithubUser']"}),
            'private': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['github_analysis']