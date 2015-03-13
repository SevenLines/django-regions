# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):
    """
    adds haversine function to quickly find ditance between objects
    """
    dependencies = [
        ('regions', '0005_auto_20150313_1042'),
    ]

    operations = [
        migrations.RunSQL(
"""
create DEFINER = CURRENT_USER function haversine (lat1 double, lon1 double, lat2 double, lon2 double) returns double
return  6371 * 2 * ASIN(SQRT(POWER(SIN((lat1 - abs(lat2)) * pi()/180 / 2), 2)
         + COS(abs(lat1) * pi()/180 ) * COS(abs(lat2) * pi()/180) * POWER(SIN((lon1 - lon2) * pi()/180 / 2), 2) )) ;
""",
"""
DROP FUNCTION haversine
"""
        )
    ]
