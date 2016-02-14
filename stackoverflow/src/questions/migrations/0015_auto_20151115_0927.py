# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0014_auto_20151115_0925'),
    ]

    operations = [
        migrations.RenameField(
            model_name='answer',
            old_name='authyor_id',
            new_name='author_id',
        ),
        migrations.RenameField(
            model_name='question',
            old_name='authorr',
            new_name='author',
        ),
    ]
