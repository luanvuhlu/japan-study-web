# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('japanstudy', '0003_auto_20150611_1300'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addwordsession',
            name='current',
            field=models.BooleanField(default=True, verbose_name=b'\xc4\x90ang s\xe1\xbb\xad d\xe1\xbb\xa5ng'),
        ),
    ]
