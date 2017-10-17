from django.contrib import admin

from .models import Page
from .models import Tag

# Register your models here.

class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'webKey', 'public', 'sample', 'assignment', 'save_count', 'created', 'lastUpdated')

admin.site.register(Page, PageAdmin)

class TagAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug')

admin.site.register(Tag, TagAdmin)
