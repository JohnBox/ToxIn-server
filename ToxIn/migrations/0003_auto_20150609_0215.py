# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ToxIn', '0002_auto_20150609_0211'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='birth',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='position',
        ),
    ]
