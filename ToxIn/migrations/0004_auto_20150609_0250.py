# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ToxIn', '0003_auto_20150609_0215'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='hide_email',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='position',
            field=models.CharField(blank=True, max_length=40),
        ),
    ]
