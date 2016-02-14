# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import loginsys.models


class Migration(migrations.Migration):

    dependencies = [
        ('loginsys', '0005_remove_userprofile_website'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='avatar',
            field=models.ImageField(null=True, upload_to=loginsys.models.get_image_path, blank=True),
        ),
    ]
