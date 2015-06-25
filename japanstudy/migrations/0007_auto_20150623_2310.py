# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('japanstudy', '0006_auto_20150623_2244'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testingword',
            name='word',
            field=models.ForeignKey(verbose_name=b'T\xe1\xbb\xab g\xe1\xbb\x91c', to='japanstudy.JapaneseWord'),
        ),
        migrations.AlterField(
            model_name='testsessionwordorder',
            name='word',
            field=models.ForeignKey(verbose_name=b'T\xe1\xbb\xab', to='japanstudy.JapaneseWord'),
        ),
        migrations.AlterField(
            model_name='testword',
            name='words',
            field=models.ManyToManyField(to='japanstudy.JapaneseWord', verbose_name=b'G\xe1\xbb\x93m c\xc3\xa1c t\xe1\xbb\xab'),
        ),
    ]
