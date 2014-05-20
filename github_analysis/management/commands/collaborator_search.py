from django.core.management.base import BaseCommand, CommandError
from django.core.exceptions import ObjectDoesNotExist
from django.conf import settings
from optparse import make_option
from github import Github
import time

from github_analysis.models import GithubUser, Repository, Contribution

class Command(BaseCommand):
    option_list = BaseCommand.option_list + (
        make_option('--user',
            type="string",
            dest="user",
            help="What user should we discover stats about?"
        ),
    )

    def handle(self, *args, **options):
        user = options['user']
        if user == None and len(args) == 0:
            self.stderr.write("You must specify a user")
            exit()
        else:
            user = args[0]
        self.stdout.write("Calculating collaboration statistics for %s" % user)

        user = GithubUser.objects.get(login=user)

        collabs = {}
        projects = 0
        for project in user.contribution_set.all():
            for u in project.repo.contribution_set.all():
                if u.user == user:
                    continue
                if u.user in collabs:
                    collabs[u.user] += 1
                else:
                    collabs[u.user] = 1
                projects += 1
                if projects % 10 == 0:
                  self.stdout.write(".", ending="")
                  self.stdout.flush()

        self.stdout.write("%s collaborated with..." % user.__unicode__())
        for key,value in sorted(collabs.items()):
            self.stdout.write("Collaborated with %s %s times" % (key.__unicode__(), value))
