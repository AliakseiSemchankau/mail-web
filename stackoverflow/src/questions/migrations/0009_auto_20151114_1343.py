# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0008_question_likers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='likers',
            field=models.ManyToManyField(to='loginsys.UserProfile'),
        ),
    ]
