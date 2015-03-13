import random
from django.contrib.gis.geos import Point
from django.contrib.gis.geos.polygon import Polygon
from django.core.management.base import BaseCommand
from django.db.transaction import atomic
import sys
from regions.models import Region


class Command(BaseCommand):
    """
    generate 100000 regions
    """
    @atomic
    def handle(self, *args, **options):
        count = 100000
        for i in xrange(count):
            lradius = random.uniform(0.1, 0.8)
            lat = random.uniform(5, 85)
            lng = random.uniform(-175, 175)

            north_east = Point(lng + lradius, lat - lradius)
            south_west = Point(lng - lradius, lat + lradius)
            center = Point(lng, lat)
            radius = lradius * 111131 # length of lng degree on 45 lat
            polygon = Polygon((
                (north_east.x, north_east.y),
                (north_east.x, south_west.y),
                (south_west.x, south_west.y),
                (south_west.x, north_east.y),
                (north_east.x, north_east.y)
            ))
            is_circle = random.randint(0,1) == 1

            region = Region(
                name="region_num_%s" % i,
                north_east =north_east,
                south_west=south_west,
                polygon=polygon,
                radius=radius,
                center=center,
                is_circle=is_circle,
            )

            percents = (float(i) / float(count)) * 100
            sys.stdout.write("Completeness: %3d%%\r" % percents)
            sys.stdout.flush()
            region.save()