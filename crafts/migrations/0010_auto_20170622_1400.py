# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crafts', '0009_auto_20160329_1500'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('order', models.PositiveIntegerField(help_text='Enter a number.')),
                ('title', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='SubCategory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('order', models.PositiveIntegerField(help_text='Enter a number.')),
                ('title', models.CharField(max_length=100, null=True)),
                ('category', models.ForeignKey(to='crafts.Category', on_delete=models.CASCADE)),
            ],
        ),
        migrations.RemoveField(
            model_name='craftpost',
            name='postcategory',
        ),
        migrations.AddField(
            model_name='craftpost',
            name='category',
            field=models.ForeignKey(to='crafts.Category', blank=True, null=True, on_delete=models.CASCADE),
        ),
        migrations.AddField(
            model_name='craftpost',
            name='subcategory',
            field=models.ForeignKey(to='crafts.SubCategory', blank=True, null=True, on_delete=models.CASCADE),
        ),
    ]
