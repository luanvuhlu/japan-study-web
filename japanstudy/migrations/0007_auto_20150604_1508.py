# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('japanstudy', '0006_auto_20150604_1426'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tag',
            name='create_time',
        ),
        migrations.RemoveField(
            model_name='word',
            name='create_time',
        ),
        migrations.AddField(
            model_name='tag',
            name='created_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 4, 8, 8, 19, 446000, tzinfo=utc), verbose_name=b'Ng\xc3\xa0y t\xe1\xba\xa1o', blank=True),
        ),
        migrations.AddField(
            model_name='word',
            name='created_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 4, 8, 8, 19, 447000, tzinfo=utc), verbose_name=b'Ng\xc3\xa0y t\xe1\xba\xa1o', blank=True),
        ),
    ]
