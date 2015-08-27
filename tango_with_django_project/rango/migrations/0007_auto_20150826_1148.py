# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0006_userprofile'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='first_visit',
            field=models.DateTimeField(default=datetime.datetime.now, blank=True),
        ),
        migrations.AddField(
            model_name='page',
            name='last_visit',
            field=models.DateTimeField(default=datetime.datetime.now, blank=True),
        ),
    ]
