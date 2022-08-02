from django.contrib import admin
from .models import *


class PortfolioAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'summary', 'skill', 'slug', 'created_on', 'votes')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'summary')
    prepopulated_fields = {"slug": ("title",)}


class SkillAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'slug')
    list_display_links = ('id', 'title')
    search_fields = ('title',)
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(Portfolio, PortfolioAdmin)

admin.site.register(Skill, SkillAdmin)
