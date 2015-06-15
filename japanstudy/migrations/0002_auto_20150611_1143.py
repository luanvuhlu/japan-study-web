# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('japanstudy', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AddWordSession',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('current', models.BooleanField(default=True, verbose_name=b'Ho\xc3\xa0n th\xc3\xa0nh')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name=b'Ng\xc3\xa0y t\xe1\xba\xa1o')),
                ('active', models.CharField(default=b'Y', max_length=2, verbose_name=b'Tr\xe1\xba\xa1ng th\xc3\xa1i', choices=[(b'Y', b'Y'), (b'N', b'N')])),
                ('user', models.ForeignKey(verbose_name=b'Ng\xc6\xb0\xe1\xbb\x9di t\xe1\xba\xa1o', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='word',
            name='temp',
            field=models.BooleanField(default=False, verbose_name=b'D\xe1\xbb\xaf li\xe1\xbb\x87u t\xe1\xba\xa1m'),
        ),
        migrations.AlterField(
            model_name='testsession',
            name='current_word',
            field=models.ForeignKey(verbose_name=b'T\xe1\xbb\xab \xc4\x91ang test', blank=True, to='japanstudy.Word', null=True),
        ),
        migrations.AddField(
            model_name='addwordsession',
            name='words',
            field=models.ManyToManyField(to='japanstudy.Word', verbose_name=b'T\xe1\xbb\xab \xc4\x91\xc6\xb0\xe1\xbb\xa3c th\xc3\xaam', blank=True),
        ),
    ]
