# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0017_auto_20151115_1037'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answer',
            name='question_id',
        ),
        migrations.AddField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(to='questions.Question', null=True),
        ),
    ]
