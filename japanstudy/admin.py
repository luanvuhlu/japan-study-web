# -*- coding: utf-8 -*- 
from django.contrib import admin
from models import Tag, JapaneseWord, TestWord, TestSession, AddWordSession, TestingWord

class BaseAdmin(admin.ModelAdmin):
    def delete_model(self, request, obj):
        obj.active='N'
        obj.save()
class JapaneseWordAdmin(BaseAdmin):
    list_display=('source', 'kanji','mean', 'other_mean', 'level', 'created_time', 'active')
    readonly_fields=('user', 'created_time')
    date_hierarchy='created_time'
    list_filter=('created_time', )
    search_fields=['source', 'mean', 'kanji', 'other_mean', 'created_time']
    ordering = ('-created_time', '-active', 'level', )
    def save_model(self, request, obj, form, change):
        if not obj.id:
            obj.user=request.user
        obj.save()

class TagAdmin(BaseAdmin):
    list_display=('name', 'created_time')
    readonly_fields=('user', 'created_time')
    date_hierarchy='created_time'
    list_filter=('created_time', )
    search_fields=['name', 'created_time']
    def save_model(self, request, obj, form, change):
        if not obj.id:
            obj.user=request.user
        obj.save()

class TestWordAdmin(BaseAdmin):
    list_display=('title', 'start_date', 'completed_time')
    readonly_fields=('user', 'created_time')
    date_hierarchy='created_time'
    list_filter=('created_time', )
    search_fields=['start_date', 'created_time', 'completed_time']
    def save_model(self, request, obj, form, change):
        if not obj.id:
            obj.user=request.user
        obj.save()
class TestingWordAdmin(BaseAdmin):
    pass

class TestSessionAdmin(BaseAdmin):
    list_display=('test_word', 'created_time')
    readonly_fields=('user', 'created_time', )
    date_hierarchy='created_time'
    list_filter=('created_time', )
    search_fields=['test_session', 'created_time']
    def save_model(self, request, obj, form, change):
        if not obj.id:
            obj.current_word=obj.test_word.words.all()[0]
            obj.user=request.user
        obj.save()


# Register your models here.
admin.site.register(Tag, TagAdmin)
admin.site.register(JapaneseWord, JapaneseWordAdmin)
admin.site.register(TestWord, TestWordAdmin)
admin.site.register(TestingWord, TestingWordAdmin)
admin.site.register(TestSession, TestSessionAdmin)
