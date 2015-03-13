from django.contrib.gis.forms import ModelForm
from regions.models import Region

__author__ = 'm'


class RegionForm(ModelForm):
    class Meta:
        model = Region
        fields = ['name', 'north_east', 'south_west', 'polygon', 'center', 'radius', 'is_circle']
