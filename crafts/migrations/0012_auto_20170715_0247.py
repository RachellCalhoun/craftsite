# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crafts', '0011_auto_20170622_1456'),
    ]

    operations = [
        migrations.RenameField(
            model_name='craftpost',
            old_name='image',
            new_name='photo',
        ),
        migrations.RemoveField(
            model_name='craftpost',
            name='subcategory',
        ),
    ]
