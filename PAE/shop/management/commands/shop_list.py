from django.core.management.base import BaseCommand, CommandError
from shop.models import Shop

import csv, sys, os
from django.utils import timezone
from django.conf import settings
import django

from django.core.files import File


class Command(BaseCommand):
    help = 'Fill information about shops with promo'

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **kwargs):
        app_dir = settings.BASE_DIR+'/shop/'
        sys.path.append(app_dir)
        os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'
        django.setup()
        data = csv.reader(open(app_dir + 'shops.csv'),delimiter=',')
        logo_img_dir = settings.MEDIA_ROOT +'/logo_img/'
        for row in data:
            if row[0] != 'Name': # Ignore the header row, import everything else
                shop = Shop()
                shop.name = row[0]
                
                try:
                    f = open(logo_img_dir + row[0] +'.jpg', 'rb')
                    shop.logo_img = File(f)
                except:
                    pass
                shop.save()
