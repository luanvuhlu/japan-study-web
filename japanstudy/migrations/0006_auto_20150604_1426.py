# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('japanstudy', '0005_auto_20150604_1426'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='create_time',
            field=models.DateField(verbose_name=b'Ng\xc3\xa0y t\xe1\xba\xa1o', blank=True),
        ),
        migrations.AlterField(
            model_name='word',
            name='create_time',
            field=models.DateField(verbose_name=b'Ng\xc3\xa0y t\xe1\xba\xa1o', blank=True),
        ),
    ]
