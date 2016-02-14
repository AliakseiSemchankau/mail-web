# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0003_auto_20151107_2005'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='tag2',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='question',
            name='tag3',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
