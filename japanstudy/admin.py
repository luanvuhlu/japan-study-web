from django.contrib import admin
from models import Tag, JapaneseWord
from django.utils import timezone

class BaseAdmin(admin.ModelAdmin):
    def delete_model(self, request, obj):
        obj.active='N'
class JapaneseWordAdmin(BaseAdmin):
    list_display=('source', 'mean', 'created_time')
    readonly_fields=('user', 'created_time')
    date_hierarchy='created_time'
    list_filter=('created_time', )
    search_fields=['source', 'mean', 'created_time']
    def save_model(self, request, obj, form, change):
        if not obj.id:
            obj.created_time=timezone.now()
            obj.user=request.user
        obj.save()
    def delete_model(self, request, obj):
        super(JapaneseWordAdmin, self).delete_model()
        obj.save()
class TagAdmin(BaseAdmin):
    list_display=('name', 'created_time')
    readonly_fields=('user', 'created_time')
    date_hierarchy='created_time'
    list_filter=('created_time', )
    search_fields=['name', 'created_time']
    def save_model(self, request, obj, form, change):
        if not obj.id:
            obj.created_time=timezone.now()
            obj.user=request.user
        obj.save()
    def delete_model(self, request, obj):
        super(TagAdmin, self).delete_model()
        obj.save()
# Register your models here.
admin.site.register(Tag, TagAdmin)
admin.site.register(JapaneseWord, JapaneseWordAdmin)
