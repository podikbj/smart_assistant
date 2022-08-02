from django.db import models
from django.urls import reverse

class MyApps(models.Model):
    app_name = models.CharField(max_length=200, verbose_name='App name')
    slug = models.SlugField(max_length=100, unique=True, db_index=True, verbose_name="slug", null=True)
    summary = models.TextField(max_length=400)

    def __str__(self):
        return self.app_name

    class Meta():
        verbose_name = 'App name'
        verbose_name_plural = 'Apps names'
