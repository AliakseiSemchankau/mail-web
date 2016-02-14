# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0012_auto_20151115_0917'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='likers',
        ),
        migrations.AlterField(
            model_name='question',
            name='authorr',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True),
        ),
    ]
