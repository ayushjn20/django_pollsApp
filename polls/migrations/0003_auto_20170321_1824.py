# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_auto_20170321_1809'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='qn_text',
            new_name='question_text',
        ),
    ]
