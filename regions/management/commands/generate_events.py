from django.core.management.base import BaseCommand
from regions.models import Event

__author__ = 'm'


class Command(BaseCommand):
    def handle(self, *args, **options):
        event = Event()
        # event.location =
