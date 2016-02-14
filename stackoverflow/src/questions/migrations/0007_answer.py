# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0006_auto_20151108_0947'),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('question_id', models.IntegerField(default=0)),
                ('text', models.CharField(max_length=400)),
                ('pub_date', models.DateTimeField(default=datetime.datetime.now, verbose_name=b'date published')),
                ('author_id', models.IntegerField(default=1)),
                ('like_count', models.IntegerField(default=0)),
            ],
        ),
    ]
