# This is where you can add stuff to the admin view
from django.contrib import admin

from github_analysis.models import Repository

# ie,
admin.site.register(Repository)
