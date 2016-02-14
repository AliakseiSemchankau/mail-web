# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0009_auto_20151114_1343'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='author_id',
        ),
        migrations.AlterField(
            model_name='question',
            name='author',
            field=models.ForeignKey(to='loginsys.UserProfile'),
        ),
        migrations.AlterField(
            model_name='question',
            name='likers',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]
