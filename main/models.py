from django.db import models

class MyApps(models.Model):
    app_name = models.CharField(max_length=200, verbose_name='App name')
    url_str = models.CharField(max_length=200, verbose_name='url string', blank=True, null=True)
    summary = models.TextField(max_length=400)
    image_url = models.URLField(max_length=255, unique=True, db_index=True, verbose_name='image_url', blank=True, null=True)

    def __str__(self):
        return self.app_name

    class Meta():
        verbose_name = 'App name'
        verbose_name_plural = 'Apps names'
