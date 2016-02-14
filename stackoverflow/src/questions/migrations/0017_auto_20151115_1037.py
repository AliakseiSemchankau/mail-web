# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loginsys', '0005_remove_userprofile_website'),
        ('questions', '0016_auto_20151115_0933'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answer',
            name='author_id',
        ),
        migrations.AddField(
            model_name='answer',
            name='author',
            field=models.ForeignKey(to='loginsys.UserProfile', null=True),
        ),
    ]
