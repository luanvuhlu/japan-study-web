# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('japanstudy', '0003_auto_20150604_1423'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='create_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 4, 7, 23, 43, 737000, tzinfo=utc), verbose_name=b'Ng\xc3\xa0y t\xe1\xba\xa1o', blank=True),
        ),
        migrations.AlterField(
            model_name='word',
            name='create_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 4, 7, 23, 43, 738000, tzinfo=utc), verbose_name=b'Ng\xc3\xa0y t\xe1\xba\xa1o', blank=True),
        ),
    ]
