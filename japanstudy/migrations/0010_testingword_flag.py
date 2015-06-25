# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('japanstudy', '0009_auto_20150624_0000'),
    ]

    operations = [
        migrations.AddField(
            model_name='testingword',
            name='flag',
            field=models.BooleanField(default=False, verbose_name=b'Lo\xe1\xba\xa1i ki\xe1\xbb\x83m tra'),
        ),
    ]
