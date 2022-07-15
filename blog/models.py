from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField(auto_created=True)
    body = models.TextField(max_length=400)
    image = models.ImageField(upload_to='main/image/')
    city = models.ForeignKey('Weather', on_delete=models.PROTECT, blank=True, null=True)

    def get_absolute_url(self):
        return f'/blog/{self.id}'

    def __str__(self):
        return self.title
    class Meta():
        verbose_name = 'Blog'
        verbose_name_plural = 'Blogs'
        ordering = ['pub_date']

class Weather(models.Model):
    city_name = models.CharField(max_length=100)

    def get_absolute_url(self):
        return f'/weather/{self.id}'

    def __str__(self):
        return self.city_name

    class Meta():
        verbose_name = 'City name'
        verbose_name_plural = 'Cities names'