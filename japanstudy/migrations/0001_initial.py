# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100, verbose_name=b'T\xc3\xaan')),
                ('description', models.TextField(max_length=500, verbose_name=b'M\xc3\xb4 t\xe1\xba\xa3', blank=True)),
                ('create_time', models.DateTimeField(default=datetime.datetime(2015, 6, 4, 7, 7, 47, 822000, tzinfo=utc), verbose_name=b'Ng\xc3\xa0y t\xe1\xba\xa1o', blank=True)),
                ('active', models.CharField(default=b'Y', max_length=2, verbose_name=b'Tr\xe1\xba\xa1ng th\xc3\xa1i', choices=[(b'Y', b'Y'), (b'N', b'N')])),
                ('user', models.ForeignKey(verbose_name=b'Ng\xc6\xb0\xe1\xbb\x9di t\xe1\xba\xa1o', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Word',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('source', models.CharField(max_length=200, verbose_name=b'T\xe1\xbb\xab')),
                ('mean', models.CharField(max_length=200, verbose_name=b'Ngh\xc4\xa9a')),
                ('description', models.TextField(max_length=500, verbose_name=b'M\xc3\xb4 t\xe1\xba\xa3', blank=True)),
                ('create_time', models.DateTimeField(default=datetime.datetime(2015, 6, 4, 7, 7, 47, 823000, tzinfo=utc), verbose_name=b'Ng\xc3\xa0y t\xe1\xba\xa1o', blank=True)),
                ('active', models.CharField(default=b'Y', max_length=2, verbose_name=b'Tr\xe1\xba\xa1ng th\xc3\xa1i', choices=[(b'Y', b'Y'), (b'N', b'N')])),
            ],
        ),
        migrations.CreateModel(
            name='JapaneseWord',
            fields=[
                ('word_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='japanstudy.Word')),
                ('kanji', models.CharField(max_length=200, verbose_name=b'T\xe1\xbb\xab Kanji', blank=True)),
                ('type', models.BooleanField(default=True, verbose_name=b'Lo\xe1\xba\xa1i t\xe1\xbb\xab', choices=[(True, b'hiragana'), (False, b'katakana')])),
            ],
            bases=('japanstudy.word',),
        ),
        migrations.AddField(
            model_name='word',
            name='tags',
            field=models.ManyToManyField(to='japanstudy.Tag', verbose_name=b'Tag', blank=True),
        ),
        migrations.AddField(
            model_name='word',
            name='user',
            field=models.ForeignKey(verbose_name=b'Ng\xc6\xb0\xe1\xbb\x9di t\xe1\xba\xa1o', to=settings.AUTH_USER_MODEL),
        ),
    ]
