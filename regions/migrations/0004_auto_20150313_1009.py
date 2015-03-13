# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.contrib.gis.db.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('regions', '0003_auto_20150313_0417'),
    ]

    operations = [
        migrations.AlterField(
            model_name='region',
            name='center',
            field=django.contrib.gis.db.models.fields.PointField(srid=4326),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='region',
            name='north_east',
            field=django.contrib.gis.db.models.fields.PointField(srid=4326),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='region',
            name='polygon',
            field=django.contrib.gis.db.models.fields.PolygonField(srid=4326),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='region',
            name='south_west',
            field=django.contrib.gis.db.models.fields.PointField(srid=4326),
            preserve_default=True,
        ),
    ]
