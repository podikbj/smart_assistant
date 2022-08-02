from django.contrib import admin

from .models import *

class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'context', 'created_on', 'deadline_day', 'deadline_time')
    list_display_links = ('id', 'context', 'created_on')
    search_fields = ('id', 'context')

admin.site.register(Task, TaskAdmin)
