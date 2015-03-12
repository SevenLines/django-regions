from django.contrib.gis.db import models


class Region(models.Model):
    name = models.CharField(max_length=128)
    north_east = models.PointField()
    south_west = models.PointField()
    polygon = models.PolygonField()

    objects = models.GeoManager()