# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0005_auto_20151108_0940'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tag',
            old_name='articles',
            new_name='questions',
        ),
    ]
