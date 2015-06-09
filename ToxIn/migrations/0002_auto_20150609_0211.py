# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ToxIn', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='birth',
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='position',
            field=models.CharField(choices=[('S', 'Студент'), ('T', 'Викладач')], max_length=1, blank=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='workplace',
            field=models.CharField(blank=True, max_length=80),
        ),
    ]
