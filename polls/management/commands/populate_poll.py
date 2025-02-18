from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from polls.models import Poll, Choice, Vote
from django.utils import timezone


class Command(BaseCommand):
    help = 'Populate the database with dummy poll data'

    def handle(self, *args, **kwargs):
        # Create users manually
        user1 = User.objects.create(username='john_doe', email='john@example.com', password='password123')
        user2 = User.objects.create(username='jane_doe', email='jane@example.com', password='password123')
        user3 = User.objects.create(username='alice_smith', email='alice@example.com', password='password123')
        user4 = User.objects.create(username='bob_jones', email='bob@example.com', password='password123')
        user5 = User.objects.create(username='charlie_brown', email='charlie@example.com', password='password123')

        # Poll 1
        poll1 = Poll.objects.create(question="What's your favorite programming language?", created_by=user1, pub_date=timezone.now())
        Choice.objects.create(poll=poll1, choice_text="Python")
        Choice.objects.create(poll=poll1, choice_text="JavaScript")
        Choice.objects.create(poll=poll1, choice_text="Ruby")
        Choice.objects.create(poll=poll1, choice_text="Java")

        # Poll 2
        poll2 = Poll.objects.create(question="What's your favorite web framework?", created_by=user2, pub_date=timezone.now())
        Choice.objects.create(poll=poll2, choice_text="Django")
        Choice.objects.create(poll=poll2, choice_text="React")
        Choice.objects.create(poll=poll2, choice_text="Flask")
        Choice.objects.create(poll=poll2, choice_text="Vue")

        # Poll 3
        poll3 = Poll.objects.create(question="What's your favorite database?", created_by=user3, pub_date=timezone.now())
        Choice.objects.create(poll=poll3, choice_text="PostgreSQL")
        Choice.objects.create(poll=poll3, choice_text="MySQL")
        Choice.objects.create(poll=poll3, choice_text="SQLite")
        Choice.objects.create(poll=poll3, choice_text="MongoDB")

        # Poll 4
        poll4 = Poll.objects.create(question="What's your favorite IDE?", created_by=user4, pub_date=timezone.now())
        Choice.objects.create(poll=poll4, choice_text="VSCode")
        Choice.objects.create(poll=poll4, choice_text="PyCharm")
        Choice.objects.create(poll=poll4, choice_text="Sublime Text")
        Choice.objects.create(poll=poll4, choice_text="Atom")

        # Poll 5
        poll5 = Poll.objects.create(question="What's your favorite operating system?", created_by=user5, pub_date=timezone.now())
        Choice.objects.create(poll=poll5, choice_text="Linux")
        Choice.objects.create(poll=poll5, choice_text="Windows")
        Choice.objects.create(poll=poll5, choice_text="macOS")
        Choice.objects.create(poll=poll5, choice_text="Chrome OS")

        # Assign votes to Poll 1
        Vote.objects.create(poll=poll1, choice=Choice.objects.get(poll=poll1, choice_text="Python"), voted_by=user1)
        Vote.objects.create(poll=poll1, choice=Choice.objects.get(poll=poll1, choice_text="JavaScript"), voted_by=user2)
        Vote.objects.create(poll=poll1, choice=Choice.objects.get(poll=poll1, choice_text="Ruby"), voted_by=user3)
        Vote.objects.create(poll=poll1, choice=Choice.objects.get(poll=poll1, choice_text="Python"), voted_by=user4)

        # Assign votes to Poll 2
        Vote.objects.create(poll=poll2, choice=Choice.objects.get(poll=poll2, choice_text="Django"), voted_by=user1)
        Vote.objects.create(poll=poll2, choice=Choice.objects.get(poll=poll2, choice_text="React"), voted_by=user2)
        Vote.objects.create(poll=poll2, choice=Choice.objects.get(poll=poll2, choice_text="Flask"), voted_by=user3)
        Vote.objects.create(poll=poll2, choice=Choice.objects.get(poll=poll2, choice_text="Vue"), voted_by=user4)

        # Assign votes to Poll 3
        Vote.objects.create(poll=poll3, choice=Choice.objects.get(poll=poll3, choice_text="PostgreSQL"), voted_by=user1)
        Vote.objects.create(poll=poll3, choice=Choice.objects.get(poll=poll3, choice_text="MySQL"), voted_by=user2)
        Vote.objects.create(poll=poll3, choice=Choice.objects.get(poll=poll3, choice_text="SQLite"), voted_by=user3)
        Vote.objects.create(poll=poll3, choice=Choice.objects.get(poll=poll3, choice_text="MongoDB"), voted_by=user4)

        # Assign votes to Poll 4
        Vote.objects.create(poll=poll4, choice=Choice.objects.get(poll=poll4, choice_text="VSCode"), voted_by=user1)
        Vote.objects.create(poll=poll4, choice=Choice.objects.get(poll=poll4, choice_text="PyCharm"), voted_by=user2)
        Vote.objects.create(poll=poll4, choice=Choice.objects.get(poll=poll4, choice_text="Sublime Text"), voted_by=user3)
        Vote.objects.create(poll=poll4, choice=Choice.objects.get(poll=poll4, choice_text="Atom"), voted_by=user4)

        # Assign votes to Poll 5
        Vote.objects.create(poll=poll5, choice=Choice.objects.get(poll=poll5, choice_text="Linux"), voted_by=user1)
        Vote.objects.create(poll=poll5, choice=Choice.objects.get(poll=poll5, choice_text="Windows"), voted_by=user2)
        Vote.objects.create(poll=poll5, choice=Choice.objects.get(poll=poll5, choice_text="macOS"), voted_by=user3)
        Vote.objects.create(poll=poll5, choice=Choice.objects.get(poll=poll5, choice_text="Chrome OS"), voted_by=user4)

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with dummy poll data'))
