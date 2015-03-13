from django.contrib.gis.db import models


class Region(models.Model):
    name = models.CharField(max_length=128)
    north_east = models.PointField(null=True, blank=True)
    south_west = models.PointField(null=True, blank=True)
    polygon = models.PolygonField(null=True, blank=True)

    is_circle = models.BooleanField(default=False)
    radius = models.FloatField(default=0, null=True, blank=True)
    center = models.PointField(null=True, blank=True)

    objects = models.GeoManager()