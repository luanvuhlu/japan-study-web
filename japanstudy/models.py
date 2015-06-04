# -*- coding: utf-8 -*- 
from django.db import models
from django.contrib.auth.models import User 
from django.core.validators import MinValueValidator
STATUS=(('Y', 'Y'), ('N', 'N'))
JAPANESE_WORD_TYPE=((True, 'Hiragana'), (False, 'Katakana'))
class Tag(models.Model):
    name=models.CharField(max_length=100, blank=False, verbose_name="Tên")
    description=models.TextField(max_length=500, blank=True, verbose_name="Mô tả")
    active=models.CharField(max_length=2, choices=STATUS, default='Y', verbose_name="Trạng thái")
    created_time=models.DateTimeField(blank=True, verbose_name="Ngày tạo")
    user=models.ForeignKey(User, verbose_name="Người tạo")
    def __unicode__(self):
        return self.name
class Word(models.Model):
    source=models.CharField(max_length=200, blank=False, verbose_name="Từ")
    mean=models.CharField(max_length=200, blank=False, verbose_name="Nghĩa")
    level=models.PositiveSmallIntegerField(validators =[MinValueValidator(0)], default=0, blank=False, verbose_name="Độ khó")
    description=models.TextField(max_length=500, blank=True, verbose_name="Mô tả")
    user=models.ForeignKey(User, verbose_name="Người tạo")
    tags=models.ManyToManyField(Tag, blank=True, verbose_name="Tag")
    sames=models.ManyToManyField('self', blank=True, verbose_name="Từ cùng nghĩa")
    created_time=models.DateTimeField(blank=True, verbose_name="Ngày tạo")
    active=models.CharField(max_length=2, choices=STATUS, default='Y', verbose_name="Trạng thái")
    def __unicode__(self):
        return self.source
class JapaneseWord(Word):
    kanji=models.CharField(max_length=200, blank=True, verbose_name="Từ Kanji")
    type=models.BooleanField(default=True, choices=JAPANESE_WORD_TYPE, verbose_name="Loại từ", blank=False)
class TestWord(models.Model):
    words=models.ManyToManyField(Word, blank=False, verbose_name="Gồm các từ")
    start_date=models.DateField(blank=True, verbose_name="Ngày bắt đầu")
    completed_time=models.DateTimeField(blank=True, verbose_name="Ngày hoàn thành")
    created_time=models.DateTimeField(blank=True, verbose_name="Ngày tạo")
    active=models.CharField(max_length=2, choices=STATUS, default='Y', verbose_name="Trạng thái")