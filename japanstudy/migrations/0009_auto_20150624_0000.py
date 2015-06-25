# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('japanstudy', '0008_testsession_completed_time'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='testresult',
            name='test_session',
        ),
        migrations.DeleteModel(
            name='TestResult',
        ),
    ]
