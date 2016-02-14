# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0013_auto_20151115_0919'),
    ]

    operations = [
        migrations.RenameField(
            model_name='answer',
            old_name='author_id',
            new_name='authyor_id',
        ),
    ]
