# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='date_birth',
            field=models.DateField(),
        ),
    ]
