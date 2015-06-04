from django.contrib import admin
from models import Tag, JapaneseWord, TestWord
from django.utils import timezone

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
    ordering = ('-active', 'level', 'created_time', )
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
    list_display=('start_date', 'completed_time')
    readonly_fields=('user', 'created_time')
    date_hierarchy='created_time'
    list_filter=('created_time', )
    search_fields=['start_date', 'created_time', 'completed_time']
    def save_model(self, request, obj, form, change):
        if not obj.id:
            obj.user=request.user
        obj.save()

# Register your models here.
admin.site.register(Tag, TagAdmin)
admin.site.register(JapaneseWord, JapaneseWordAdmin)
admin.site.register(TestWord, TestWordAdmin)
