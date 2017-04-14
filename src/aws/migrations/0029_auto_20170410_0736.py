# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aws', '0028_auto_20170410_0736'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aws',
            name='user_id',
            field=models.IntegerField(serialize=False, primary_key=True, blank=True),
        ),
    ]
