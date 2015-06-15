# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('japanstudy', '0002_auto_20150611_1143'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='addwordsession',
            name='words',
        ),
        migrations.AddField(
            model_name='addwordsession',
            name='japanese_words',
            field=models.ManyToManyField(to='japanstudy.JapaneseWord', verbose_name=b'T\xe1\xbb\xab \xc4\x91\xc6\xb0\xe1\xbb\xa3c th\xc3\xaam', blank=True),
        ),
    ]
