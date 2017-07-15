# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crafts', '0010_auto_20170622_1400'),
    ]

    operations = [
        migrations.RenameField(
            model_name='craftpost',
            old_name='photo',
            new_name='image',
        ),
    ]
