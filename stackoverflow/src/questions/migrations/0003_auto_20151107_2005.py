# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0002_auto_20151030_2026'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='tag1',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name=b'date published'),
        ),
    ]
