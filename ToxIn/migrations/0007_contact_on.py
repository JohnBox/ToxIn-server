# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ToxIn', '0006_contact'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='on',
            field=models.BooleanField(default=False),
        ),
    ]
