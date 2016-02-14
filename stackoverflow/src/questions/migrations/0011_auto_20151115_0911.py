# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0010_auto_20151115_0901'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='author',
            new_name='authorr',
        ),
    ]
