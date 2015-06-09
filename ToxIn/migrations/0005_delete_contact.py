# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ToxIn', '0004_auto_20150609_0250'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Contact',
        ),
    ]
