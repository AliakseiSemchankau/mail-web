# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='choice',
            name='question',
        ),
        migrations.RenameField(
            model_name='question',
            old_name='question_author',
            new_name='author',
        ),
        migrations.RenameField(
            model_name='question',
            old_name='question_name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='question',
            old_name='question_text',
            new_name='text',
        ),
        migrations.AddField(
            model_name='question',
            name='answer_count',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='question',
            name='author_id',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='question',
            name='like_count',
            field=models.IntegerField(default=0),
        ),
        migrations.DeleteModel(
            name='Choice',
        ),
    ]
