# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import django.core.validators


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
                ('description', models.TextField(max_length=500, null=True, verbose_name=b'M\xc3\xb4 t\xe1\xba\xa3', blank=True)),
                ('active', models.CharField(default=b'Y', max_length=2, verbose_name=b'Tr\xe1\xba\xa1ng th\xc3\xa1i', choices=[(b'Y', b'Y'), (b'N', b'N')])),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name=b'Ng\xc3\xa0y t\xe1\xba\xa1o')),
                ('user', models.ForeignKey(verbose_name=b'Ng\xc6\xb0\xe1\xbb\x9di t\xe1\xba\xa1o', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='TestResult',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('correct', models.PositiveSmallIntegerField(verbose_name=b'S\xe1\xbb\x91 c\xc3\xa2u \xc4\x91\xc3\xbang', validators=[django.core.validators.MinValueValidator(0)])),
                ('incorrect', models.PositiveSmallIntegerField(verbose_name=b'S\xe1\xbb\x91 c\xc3\xa2u sai', validators=[django.core.validators.MinValueValidator(0)])),
                ('break_words', models.PositiveSmallIntegerField(verbose_name=b'S\xe1\xbb\x91 b\xe1\xbb\x8f qua', validators=[django.core.validators.MinValueValidator(0)])),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name=b'Ng\xc3\xa0y t\xe1\xba\xa1o')),
            ],
        ),
        migrations.CreateModel(
            name='TestSession',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('start', models.DateTimeField(null=True, verbose_name=b'B\xe1\xba\xaft ', blank=True)),
                ('end', models.DateTimeField(null=True, verbose_name=b'K\xe1\xba\xbft th\xc3\xbac', blank=True)),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name=b'Ng\xc3\xa0y t\xe1\xba\xa1o')),
            ],
        ),
        migrations.CreateModel(
            name='TestWord',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200, verbose_name=b'Ti\xc3\xaau \xc4\x91\xe1\xbb\x81 best')),
                ('start_date', models.DateTimeField(null=True, verbose_name=b'Ng\xc3\xa0y b\xe1\xba\xaft \xc4\x91\xe1\xba\xa7u', blank=True)),
                ('completed_time', models.DateTimeField(null=True, verbose_name=b'Ng\xc3\xa0y ho\xc3\xa0n th\xc3\xa0nh', blank=True)),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name=b'Ng\xc3\xa0y t\xe1\xba\xa1o')),
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
                ('other_mean', models.TextField(max_length=500, null=True, verbose_name=b'Ngh\xc4\xa9a kh\xc3\xa1c', blank=True)),
                ('level', models.PositiveSmallIntegerField(default=0, verbose_name=b'\xc4\x90\xe1\xbb\x99 kh\xc3\xb3', validators=[django.core.validators.MinValueValidator(0)])),
                ('description', models.TextField(max_length=500, null=True, verbose_name=b'M\xc3\xb4 t\xe1\xba\xa3', blank=True)),
                ('example', models.TextField(max_length=500, null=True, verbose_name=b'V\xc3\xad d\xe1\xbb\xa5', blank=True)),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name=b'Ng\xc3\xa0y t\xe1\xba\xa1o')),
                ('active', models.CharField(default=b'Y', max_length=2, verbose_name=b'Tr\xe1\xba\xa1ng th\xc3\xa1i', choices=[(b'Y', b'Y'), (b'N', b'N')])),
            ],
        ),
        migrations.CreateModel(
            name='WordTesting',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('start', models.DateTimeField(null=True, verbose_name=b'B\xe1\xba\xaft ', blank=True)),
                ('end', models.DateTimeField(null=True, verbose_name=b'K\xe1\xba\xbft th\xc3\xbac', blank=True)),
                ('correct', models.BooleanField(verbose_name=b'Ch\xc3\xadnh x\xc3\xa1c')),
                ('complete', models.BooleanField(default=False, verbose_name=b'Ho\xc3\xa0n th\xc3\xa0nh')),
                ('test_session', models.ForeignKey(verbose_name=b'Phi\xc3\xaan test', to='japanstudy.TestSession')),
            ],
        ),
        migrations.CreateModel(
            name='JapaneseWord',
            fields=[
                ('word_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='japanstudy.Word')),
                ('kanji', models.CharField(max_length=200, null=True, verbose_name=b'T\xe1\xbb\xab Kanji', blank=True)),
                ('romaji', models.CharField(max_length=200, null=True, verbose_name=b'Phi\xc3\xaan \xc3\xa2m Latinh', blank=True)),
                ('type', models.BooleanField(default=True, verbose_name=b'Lo\xe1\xba\xa1i t\xe1\xbb\xab', choices=[(True, b'Hiragana'), (False, b'Katakana')])),
            ],
            bases=('japanstudy.word',),
        ),
        migrations.AddField(
            model_name='wordtesting',
            name='word',
            field=models.ForeignKey(verbose_name=b'T\xe1\xbb\xab', to='japanstudy.Word'),
        ),
        migrations.AddField(
            model_name='word',
            name='sames',
            field=models.ManyToManyField(related_name='sames_rel_+', verbose_name=b'T\xe1\xbb\xab c\xc3\xb9ng ngh\xc4\xa9a', to='japanstudy.Word', blank=True),
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
        migrations.AddField(
            model_name='testword',
            name='words',
            field=models.ManyToManyField(to='japanstudy.Word', verbose_name=b'G\xe1\xbb\x93m c\xc3\xa1c t\xe1\xbb\xab'),
        ),
        migrations.AddField(
            model_name='testsession',
            name='current_word',
            field=models.ForeignKey(verbose_name=b'T\xe1\xbb\xab \xc4\x91ang test', to='japanstudy.Word'),
        ),
        migrations.AddField(
            model_name='testsession',
            name='test_word',
            field=models.ForeignKey(verbose_name=b'B\xc3\xa0i test', to='japanstudy.TestWord'),
        ),
        migrations.AddField(
            model_name='testsession',
            name='user',
            field=models.ForeignKey(verbose_name=b'Ng\xc6\xb0\xe1\xbb\x9di t\xe1\xba\xa1o', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='testresult',
            name='test_session',
            field=models.ForeignKey(verbose_name=b'Phi\xc3\xaan test', to='japanstudy.TestSession'),
        ),
    ]
