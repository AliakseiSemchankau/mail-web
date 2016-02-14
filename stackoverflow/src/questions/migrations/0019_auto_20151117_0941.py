# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0018_auto_20151115_1908'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='question',
            name='text',
            field=models.CharField(max_length=500),
        ),
    ]
