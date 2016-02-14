# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0011_auto_20151115_0911'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='authorr',
            field=models.ForeignKey(to='loginsys.UserProfile', null=True),
        ),
    ]
