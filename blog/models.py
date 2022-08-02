from django.db import models
from django.utils import timezone
import datetime
from django.urls import reverse


class Blog(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField(auto_created=True)
    body = models.TextField(max_length=400)
    image = models.ImageField(upload_to='images_blog/%Y/%m/%d/')
    city = models.ForeignKey('Cities', on_delete=models.PROTECT, blank=True, null=True)
    votes = models.IntegerField(default=0)

    def get_absolute_url(self):
        return reverse('blog_details', kwargs={'blog_id': self.pk})

    def __str__(self):
        return self.title

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    def summary(self):
        return self.body[:100]

    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %e %Y')

    class Meta():
        verbose_name = 'Blog'
        verbose_name_plural = 'Blogs'
        ordering = ['pub_date']


class Cities(models.Model):
    city_name = models.CharField(max_length=100)
    lon = models.FloatField(default=0)
    lat = models.FloatField(default=0)

    def get_absolute_url(self):
        return reverse('city', kwargs={'city_id': self.pk})

    def __str__(self):
        return self.city_name

    class Meta():
        verbose_name = 'City name'
        verbose_name_plural = 'Cities names'
