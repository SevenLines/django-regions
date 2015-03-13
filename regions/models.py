from django.contrib.gis.db import models


class Region(models.Model):
    name = models.CharField(max_length=128)
    north_east = models.PointField()
    south_west = models.PointField()
    polygon = models.PolygonField()

    is_circle = models.BooleanField(default=False)
    radius = models.FloatField(default=0, null=True, blank=True)
    center = models.PointField()

    objects = models.GeoManager()