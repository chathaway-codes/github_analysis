from django.core.management.base import BaseCommand, CommandError
from django.core.exceptions import ObjectDoesNotExist
from django.conf import settings
from optparse import make_option
from github import Github
import time

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
        prev_time = time.time()
        prev_api = g.get_rate_limit().rate.remaining

        total_avg_api_calls = 0
        total_counter = 0

        for repo in g.get_repos(since=self.start):
            self.save_repo(repo)
            cur_time = time.time()
            time_elapsed = cur_time-prev_time
            if time_elapsed > 10:
                cur_api = g.get_rate_limit().rate.remaining
                avg_api = (prev_api-cur_api)/float(time_elapsed)
                prev_api = cur_api
                total_avg_api_calls += avg_api
                total_counter += 1
                prev_time = cur_time
                self.stdout.write("Average API requests/second: %s\n" % (avg_api))
                self.stdout.write("Total average so far: %s\n" % (total_avg_api_calls/total_counter))

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
        stats = g_repo.get_contributors()
        if stats == None:
            return
        for u in stats:
            user = self.save_user(u)

            if Contribution.objects.filter(user=user, repo=repo).count() != 0:
                return

            self.stdout.write("Saving contribution to %s from %s" % (repo, user))
            Contribution(user=user, repo=repo, total_contributions=u.contributions).save()

    def save_user(self, g_user):
        try:
            user = GithubUser.objects.get(pk=g_user.id)
        except ObjectDoesNotExist:
            user = GithubUser()
            for f in user._meta.get_all_field_names():
                if f=='contribution' or f=='repository':
                    continue
                try:
                    v = getattr(g_user, f)
                    setattr(user, f, v)
                except AttributeError:
                    self.stderr.write("Warning: failed to find attribute %s in user object" % f)
            self.stdout.write("Saving user %s" % user.login)
            user.save()
        return user
