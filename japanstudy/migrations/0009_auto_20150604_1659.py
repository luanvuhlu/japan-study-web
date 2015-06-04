# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('japanstudy', '0008_auto_20150604_1528'),
    ]

    operations = [
        migrations.CreateModel(
            name='TestWord',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('start_date', models.DateField(verbose_name=b'Ng\xc3\xa0y b\xe1\xba\xaft \xc4\x91\xe1\xba\xa7u', blank=True)),
                ('completed_time', models.DateTimeField(verbose_name=b'Ng\xc3\xa0y ho\xc3\xa0n th\xc3\xa0nh', blank=True)),
                ('created_time', models.DateTimeField(verbose_name=b'Ng\xc3\xa0y t\xe1\xba\xa1o', blank=True)),
                ('active', models.CharField(default=b'Y', max_length=2, verbose_name=b'Tr\xe1\xba\xa1ng th\xc3\xa1i', choices=[(b'Y', b'Y'), (b'N', b'N')])),
            ],
        ),
        migrations.AddField(
            model_name='word',
            name='level',
            field=models.PositiveSmallIntegerField(default=0, verbose_name=b'\xc4\x90\xe1\xbb\x99 kh\xc3\xb3', validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='japaneseword',
            name='type',
            field=models.BooleanField(default=True, verbose_name=b'Lo\xe1\xba\xa1i t\xe1\xbb\xab', choices=[(True, b'Hiragana'), (False, b'Katakana')]),
        ),
        migrations.AddField(
            model_name='testword',
            name='words',
            field=models.ManyToManyField(to='japanstudy.Word', verbose_name=b'G\xe1\xbb\x93m c\xc3\xa1c t\xe1\xbb\xab'),
        ),
    ]
