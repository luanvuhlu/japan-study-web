# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('japanstudy', '0007_auto_20150604_1508'),
    ]

    operations = [
        migrations.AddField(
            model_name='word',
            name='sames',
            field=models.ManyToManyField(related_name='sames_rel_+', verbose_name=b'T\xe1\xbb\xab c\xc3\xb9ng ngh\xc4\xa9a', to='japanstudy.Word', blank=True),
        ),
        migrations.AlterField(
            model_name='tag',
            name='created_time',
            field=models.DateTimeField(verbose_name=b'Ng\xc3\xa0y t\xe1\xba\xa1o', blank=True),
        ),
        migrations.AlterField(
            model_name='word',
            name='created_time',
            field=models.DateTimeField(verbose_name=b'Ng\xc3\xa0y t\xe1\xba\xa1o', blank=True),
        ),
    ]
