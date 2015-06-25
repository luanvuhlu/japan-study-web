# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('japanstudy', '0005_auto_20150615_1438'),
    ]

    operations = [
        migrations.CreateModel(
            name='TestingWord',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('source', models.CharField(max_length=200, null=True, verbose_name=b'T\xe1\xbb\xab', blank=True)),
                ('mean', models.CharField(max_length=200, null=True, verbose_name=b'Ngh\xc4\xa9a', blank=True)),
                ('kanji', models.CharField(max_length=200, null=True, verbose_name=b'T\xe1\xbb\xab Kanji', blank=True)),
                ('added_time', models.DateTimeField(auto_now_add=True, verbose_name=b'Ng\xc3\xa0y th\xc3\xaam')),
                ('order', models.PositiveSmallIntegerField(verbose_name=b'Th\xe1\xbb\xa9 t\xe1\xbb\xb1')),
            ],
        ),
        migrations.CreateModel(
            name='TestSessionWordOrder',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('order', models.PositiveSmallIntegerField(verbose_name=b'Th\xe1\xbb\xa9 t\xe1\xbb\xb1')),
                ('current', models.BooleanField(default=False, verbose_name=b'T\xe1\xbb\xab hi\xe1\xbb\x87n t\xe1\xba\xa1i')),
                ('correct', models.BooleanField(default=False, verbose_name=b'Ch\xc3\xadnh x\xc3\xa1c')),
                ('completed', models.BooleanField(default=False, verbose_name=b'Ho\xc3\xa0n th\xc3\xa0nh')),
                ('start', models.DateTimeField(null=True, verbose_name=b'B\xe1\xba\xaft \xc4\x91\xe1\xba\xa7u', blank=True)),
                ('end', models.DateTimeField(null=True, verbose_name=b'K\xe1\xba\xbft th\xc3\xbac', blank=True)),
                ('word', models.ForeignKey(verbose_name=b'T\xe1\xbb\xab', to='japanstudy.Word')),
            ],
        ),
        migrations.RemoveField(
            model_name='wordtesting',
            name='test_session',
        ),
        migrations.RemoveField(
            model_name='wordtesting',
            name='word',
        ),
        migrations.RemoveField(
            model_name='testsession',
            name='current_word',
        ),
        migrations.RemoveField(
            model_name='testsession',
            name='end',
        ),
        migrations.RemoveField(
            model_name='testsession',
            name='start',
        ),
        migrations.AddField(
            model_name='testsession',
            name='completed',
            field=models.BooleanField(default=False, verbose_name=b'\xc4\x90\xc3\xa3 Ho\xc3\xa0n th\xc3\xa0nh'),
        ),
        migrations.DeleteModel(
            name='WordTesting',
        ),
        migrations.AddField(
            model_name='testingword',
            name='test_session',
            field=models.ForeignKey(verbose_name=b'Phi\xc3\xaan test', to='japanstudy.TestSession'),
        ),
        migrations.AddField(
            model_name='testingword',
            name='word',
            field=models.ForeignKey(verbose_name=b'T\xe1\xbb\xab g\xe1\xbb\x91c', to='japanstudy.Word'),
        ),
        migrations.AddField(
            model_name='testsession',
            name='test_session_word_orders',
            field=models.ManyToManyField(to='japanstudy.TestSessionWordOrder', verbose_name=b'Th\xe1\xbb\xa9 t\xe1\xbb\xb1', blank=True),
        ),
    ]
