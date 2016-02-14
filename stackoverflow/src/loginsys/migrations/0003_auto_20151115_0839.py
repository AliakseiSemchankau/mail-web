# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loginsys', '0002_userprofile_picture'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='picture',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='avatar',
            field=models.ImageField(upload_to=b'avatars', blank=True),
        ),
    ]
