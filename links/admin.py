from django.contrib import admin

from .models import *

class LinksAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category', 'sub_category', 'context', 'created_on', 'url')
    list_display_links = ('id', 'title', 'category')
    search_fields = ('id', 'title')
    list_editable = ('sub_category',)
    list_filter = ('category', )

class CategoriesAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_on')
    list_display_links = ('id', 'title')
    search_fields = ('id', 'title')
    list_filter = ('created_on', )

admin.site.register(Links, LinksAdmin)
admin.site.register(Categories, CategoriesAdmin)