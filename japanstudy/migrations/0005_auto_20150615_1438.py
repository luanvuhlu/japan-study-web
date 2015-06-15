# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('japanstudy', '0004_auto_20150611_1441'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testword',
            name='title',
            field=models.CharField(max_length=200, verbose_name=b'Ti\xc3\xaau \xc4\x91\xe1\xbb\x81'),
        ),
    ]
