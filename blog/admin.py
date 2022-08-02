from django.contrib import admin
from . models import Blog, Cities

class BlogAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'pub_date', 'image', 'city', 'votes')
    list_display_links = ('id', 'title')
    search_fields = ('id', 'title')
    list_editable = ('pub_date', 'votes')
    list_filter = ('pub_date', 'city')

admin.site.register(Blog, BlogAdmin)

class CitiesAdmin(admin.ModelAdmin):
    list_display = ('id', 'city_name', 'lon', 'lat')
    list_display_links = ('id',)
    search_fields = ('id', 'city_name')
    list_editable = ('city_name',)
    list_filter = ('city_name', )

admin.site.register(Cities, CitiesAdmin)
