# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):
    dependencies = [
        ('regions', '0004_auto_20150313_1009'),
    ]

    operations = [
        migrations.RunSQL(
            "ALTER TABLE regions_region ENGINE=MyISAM; CREATE spatial index sp_index on regions_region(polygon);",
            reverse_sql="DROP INDEX sp_index on regions_region; ALTER TABLE regions_region ENGINE=InnoDB;"),
    ]
