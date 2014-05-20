from django.core.management.base import BaseCommand, CommandError
from django.core.exceptions import ObjectDoesNotExist
from django.conf import settings
from optparse import make_option
from github import Github, GithubException
import time, os

from github_analysis.models import GithubUser, Repository, Contribution
from git import *

class GithubRepo:
  def __init__(self, url):
    self.repo = Repo(url)
    self.shas = []
  
  def get_commits(self):
    if self.shas == []:
      for commit in self.repo.iter_commits('master'):
        self.shas += [commit.hexsha]
    return self.shas
    
  def compare(self, other):
    if not isinstance(other, GithubRepo):
      raise Exception("You done messed up bloke. %s is not a GithubRepo!" % other)
    match = 0
    o_shas = other.get_commits()
    o_size = len(o_shas)
    for i, v in enumerate(self.get_commits()):
      if o_size <  i or o_shas[-1-i] != self.shas[-1-i]:
        break
      match += 1
    return match

class Command(BaseCommand):
    option_list = BaseCommand.option_list + (
        make_option('--start-at',
            type='int',
            dest='start_at',
            default=0,
            help='Which project should we start at?',
        ),
        make_option('--stop-at',
            type='int',
            dest='stop_at',
            default=Repository.objects.all().count(),
            help='Which project should we stop at?',
        ),
    )

    repo_base = '/home/chathaway/github_repos/'

    def handle(self, *args, **options):
        self.start = options['start_at']
        self.stop = options['stop_at']
        self.repos = {}

        # Load all existing repos, in order

        for repo in Repository.objects.filter(id__gte=self.start, id__lte=self.stop):
            # If the repo has not been cloned, wait until it is
            # Do the stuff
            path = os.path.join(Command.repo_base, repo.full_name.replace('/', '.')
            g_repo = GithubRepo(path)
            for key, value in self.repos:
                score = g_repo.compare(value)
                if score > 0:
                    if repo.parent == None or repo.common_parent < score:
                        repo.parent = key
                        repo.common_parent = score
            repo.save()
            self.repos[repo] = g_repo
