from django.contrib.gis.geos.point import Point
from django.core.urlresolvers import reverse
from django.test import TestCase

# Create your tests here.
from regions.models import Region


class TestViews(TestCase):

    def test_index_should_redirect_if_latlng_is_NOT_defined(self):
        response = self.client.get(reverse("regions.views.index"))
        self.assertEqual(response.status_code, 302)

    def test_index_should_respond_if_latlng_is_defined(self):
        pass

    def test_add_should_respond(self):
        response = self.client.get(reverse("regions.views.add"))
        self.assertEqual(response.status_code, 200)

    def test_update_should_respond(self):
        region = Region.objects.create(north_east=Point(0,0),
                                       south_west=Point(0,0))

        response = self.client.get(reverse("regions.views.update", args=[region.pk]))
        self.assertEqual(response.status_code, 200)
