from django.core.management import BaseCommand
from django.db import connections
from django.db.utils import OperationalError
import time


class Command(BaseCommand):
    def handle(self, *args, **options):
        self.stdout.write('Waiting for database...')
        # conn = None
        db_up = False
        
        while db_up is False:
            try:
                self.check(databases=['default'])
                db_up = True
                # conn = connections['default']
            except OperationalError:
                self.stdout.write('Database unavailable, waiting 1 second...')
                time.sleep(1)
        
        
        self.stdout.write(self.style.SUCCESS('Database available'))