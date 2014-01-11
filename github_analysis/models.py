# This is where the models go!
from django.db import models
from django.core.urlresolvers import reverse
from django.conf import settings

# Using the user: user = models.ForeignKey(settings.AUTH_USER_MODEL)

class Repository(models.Model):
    id = models.IntegerField(primary_key=True)
    owner = models.ForeignKey('github_analysis.GithubUser')
    name = models.CharField(max_length=1024)
    full_name = models.CharField(max_length=1024)
    description = models.TextField()
    private = models.BooleanField(default=False)
    fork = models.BooleanField(default=False)
    url = models.URLField()
    html_url = models.URLField()
	
    def save(self):
        if not self.description:
            self.description = " "
        super(Repository, self).save()


    def __unicode__(self):
        return self.full_name

class GithubUser(models.Model):
    login = models.CharField(max_length=1024)
    id = models.IntegerField(primary_key=True)
    gravatar_id = models.CharField(max_length=1024, null=True)
    url = models.URLField()
    html_url = models.URLField()
    followers_url = models.URLField()
    following_url = models.URLField()
    starred_url = models.URLField()
    subscriptions_url = models.URLField()
    organizations_url = models.URLField()
    repos_url = models.URLField()
    followers = models.IntegerField()
    following = models.IntegerField()

    def __unicode__(self):
        return self.login

class Contribution(models.Model):
    user = models.ForeignKey('github_analysis.GithubUser')
    repo = models.ForeignKey('github_analysis.Repository')

    total_contributions = models.IntegerField()
