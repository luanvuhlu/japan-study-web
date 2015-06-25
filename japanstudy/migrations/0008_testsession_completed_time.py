# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('japanstudy', '0007_auto_20150623_2310'),
    ]

    operations = [
        migrations.AddField(
            model_name='testsession',
            name='completed_time',
            field=models.DateTimeField(null=True, verbose_name=b'Th\xe1\xbb\x9di gian ho\xc3\xa0n th\xc3\xa0nh', blank=True),
        ),
    ]
