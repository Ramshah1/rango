# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0007_auto_20150826_1148'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='page',
            name='first_visit',
        ),
        migrations.RemoveField(
            model_name='page',
            name='last_visit',
        ),
    ]
