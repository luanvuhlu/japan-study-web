# -*- coding: utf-8 -*- 
from django.db import models
from django.contrib.auth.models import User 
from django.core.validators import MinValueValidator
from django.template.defaultfilters import default
from django.db.models import Q
STATUS = (('Y', 'Y'), ('N', 'N'))
JAPANESE_WORD_TYPE = ((True, 'Hiragana'), (False, 'Katakana'))
class Tag(models.Model):
    name = models.CharField(max_length=100, blank=False, verbose_name="Tên")
    description = models.TextField(max_length=500, null=True, blank=True, verbose_name="Mô tả")
    active = models.CharField(max_length=2, choices=STATUS, default='Y', verbose_name="Trạng thái")
    created_time = models.DateTimeField(auto_now_add=True, blank=True, verbose_name="Ngày tạo")
    user = models.ForeignKey(User, verbose_name="Người tạo")
    def __unicode__(self):
        return self.name
class Word(models.Model):
    source = models.CharField(max_length=200, blank=False, verbose_name="Từ")
    mean = models.CharField(max_length=200, blank=False, verbose_name="Nghĩa")
    other_mean = models.TextField(max_length=500, null=True, blank=True, verbose_name="Nghĩa khác")
    level = models.PositiveSmallIntegerField(validators=[MinValueValidator(0)], default=0, blank=False, verbose_name="Độ khó")
    description = models.TextField(max_length=500, null=True, blank=True, verbose_name="Mô tả")
    example = models.TextField(max_length=500, null=True, blank=True, verbose_name="Ví dụ")
    user = models.ForeignKey(User, verbose_name="Người tạo")
    tags = models.ManyToManyField(Tag, blank=True, verbose_name="Tag")
    sames = models.ManyToManyField('self', blank=True, verbose_name="Từ cùng nghĩa")
    created_time = models.DateTimeField(auto_now_add=True, blank=True, verbose_name="Ngày tạo")
    active = models.CharField(max_length=2, choices=STATUS, default='Y', verbose_name="Trạng thái")
    temp = models.BooleanField(default=False, blank=False, verbose_name="Dữ liệu tạm")
    def __unicode__(self):
        return self.source
    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        if not self.id and len(Word.objects.filter(source=self.source, mean=self.mean)):
            return
        if self.id and len(Word.objects.filter(~Q(id=self.id), source=self.source, mean=self.mean)):
            return
        return models.Model.save(self, force_insert=force_insert, force_update=force_update, using=using, update_fields=update_fields)
class JapaneseWord(Word):
    kanji = models.CharField(max_length=200, blank=True, null=True, verbose_name="Từ Kanji")
    romaji = models.CharField(max_length=200, blank=True, null=True, verbose_name="Phiên âm Latinh")
    type = models.BooleanField(default=True, choices=JAPANESE_WORD_TYPE, verbose_name="Loại từ", blank=False)
    def __unicode__(self):
        return Word.__unicode__(self)
class AddWordSession(models.Model):
    japanese_words = models.ManyToManyField(JapaneseWord, blank=True, verbose_name="Từ được thêm")
    user = models.ForeignKey(User, verbose_name="Người tạo")
    current = models.BooleanField(default=True, blank=True, verbose_name="Đang sử dụng")
    created_time = models.DateTimeField(auto_now_add=True, blank=True, verbose_name="Ngày tạo")
    active = models.CharField(max_length=2, choices=STATUS, default='Y', verbose_name="Trạng thái")
    def __unicode__(self):
        return self.user.__str__()
class TestWord(models.Model):
    title = models.CharField(max_length=200, blank=False, verbose_name="Tiêu đề")
    words = models.ManyToManyField(Word, blank=False, verbose_name="Gồm các từ")
    start_date = models.DateTimeField(null=True, blank=True, verbose_name="Ngày bắt đầu")
    completed_time = models.DateTimeField(null=True, blank=True, verbose_name="Ngày hoàn thành")
    created_time = models.DateTimeField(auto_now_add=True, blank=True, verbose_name="Ngày tạo")
    user = models.ForeignKey(User, verbose_name="Người tạo")
    active = models.CharField(max_length=2, choices=STATUS, default='Y', verbose_name="Trạng thái")
    def __unicode__(self):
        return self.title
    def get_shuffle_words(self):
        return self.words.order_by('?')
class TestSessionWordOrder(models.Model):
    order=models.PositiveSmallIntegerField(verbose_name="Thứ tự")
    word=models.ForeignKey(Word, verbose_name="Từ")
    current=models.BooleanField(default=False, verbose_name="Từ hiện tại")
    correct = models.BooleanField(default=False, blank=True, verbose_name="Chính xác")
    completed = models.BooleanField(default=False, verbose_name="Hoàn thành")
    start = models.DateTimeField(null=True, blank=True, verbose_name="Bắt đầu")
    end = models.DateTimeField(null=True, blank=True, verbose_name="Kết thúc")
    def __unicode__(self):
        return unicode(self.word) or u''
class TestSession(models.Model):
    test_word = models.ForeignKey(TestWord, verbose_name="Bài test")
    test_session_word_orders = models.ManyToManyField(TestSessionWordOrder, blank=True, verbose_name="Thứ tự")
    created_time = models.DateTimeField(auto_now_add=True, blank=True, verbose_name="Ngày tạo")
    user = models.ForeignKey(User, verbose_name="Người tạo")
    completed=models.BooleanField(default=False, verbose_name="Đã Hoàn thành")
    def __unicode__(self):
        return self.test_word.__str__() or u''

class TestResult(models.Model):
    test_session = models.ForeignKey(TestSession, verbose_name="Phiên test")
    correct = models.PositiveSmallIntegerField(validators=[MinValueValidator(0)], verbose_name="Số câu đúng")
    incorrect = models.PositiveSmallIntegerField(validators=[MinValueValidator(0)], verbose_name="Số câu sai")
    break_words = models.PositiveSmallIntegerField(validators=[MinValueValidator(0)], verbose_name="Số bỏ qua")
    created_time = models.DateTimeField(auto_now_add=True, blank=True, verbose_name="Ngày tạo")
    def __unicode__(self):
        return self.test_session.__str__() or u''
