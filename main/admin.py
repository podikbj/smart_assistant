from django.contrib import admin
from . models import MyApps

class MyAppsAdmin(admin.ModelAdmin):
    list_display = ('id', 'app_name', 'slug', 'summary')
    list_display_links = ('id', 'app_name')
    search_fields = ('app_name', 'summary')

admin.site.register(MyApps, MyAppsAdmin)

