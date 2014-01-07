from django.core.management.base import BaseCommand, CommandError
from django.core.exceptions import ObjectDoesNotExist
from django.conf import settings
from optparse import make_option
from github import Github
import json

from github_analysis.models import GithubUser, Repository, Contribution

def get_start_at():
    if Repository.objects.count() > 0:
        return Repository.objects.order_by('-id').all()[0].id-1
    return 0

class Command(BaseCommand):
    option_list = BaseCommand.option_list + (
        make_option('--start-at', 
            type='int',
            dest='start_at',
            default=get_start_at(),
            help='Which project should we stop at?',
        ),
        make_option('--stop-at',
            type='int',
            dest='stop_at',
            default=100,
            help='Which project should we stop at?',
        ),
    )

    def handle(self, *args, **options):
        self.start = options['start_at']
        self.stop = options['stop_at']
        self.current = 0

        self.g = g = Github(settings.GITHUB_TOKEN)

        for repo in g.get_repos(since=self.start):
            self.save_repo(repo)

    def save_repo(self, g_repo):
        self.stdout.write("Saving repo %s" % g_repo.full_name)

        user = self.save_user(g_repo.owner)

        try:
            repo = Repository.objects.get(pk=g_repo.id)
        except ObjectDoesNotExist:
            repo = Repository()
        for f in repo._meta.get_all_field_names():
            if f == 'owner':
                setattr(repo, f, user)
                continue
            elif f == 'contribution':
                continue
            v = getattr(g_repo, f)
            setattr(repo, f, v)
        repo.save()

        self.save_contributions(repo, g_repo)

    def save_contributions(self, repo, g_repo):
        stats = g_repo.get_stats_contributors()
        if stats == None:
            return
        for u in stats:
            user = self.save_user(u.author)

            a,d,c = 0,0,0

            for w in u.weeks:
                a += w.a
                d += w.d
                c += w.c

            self.stdout.write("Saving contribution to %s from %s" % (repo, user))
            Contribution(user=user, repo=repo, total_contributions=u.total,
                        total_changed=c, total_added=a, total_deleted=d).save()

    def save_user(self, g_user):
        try:
            user = GithubUser.objects.get(pk=g_user.id)
        except ObjectDoesNotExist:
            user = GithubUser()
            for f in user._meta.get_all_field_names():
                try:
                    v = getattr(g_user, f)
                    setattr(user, f, v)
                except AttributeError:
                    self.stderr.write("Warning: failed to find attribute %s in user object" % f)
            self.stdout.write("Saving user %s" % user.login)
            user.save()
        return user
