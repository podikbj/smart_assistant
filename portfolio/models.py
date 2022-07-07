from django.db import models
from django.urls import reverse

class Portfolio(models.Model):

    summary = models.CharField(max_length=200)
    category = models.ForeignKey('Categories', on_delete=models.PROTECT)
    url = models.URLField(max_length=255, unique=True, db_index=True, verbose_name='url', null=True)

    def __str__(self):
        return 'My '+ self.category.__str__() + 'project'
    class Meta():
        verbose_name = 'Link to a certain project'
        verbose_name_plural = 'Links to a certain projects'
        ordering = ['category']

class Categories(models.Model):
    title = models.CharField(max_length=100, db_index=True, verbose_name='title')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('category', kwargs={'category_id': self.pk})

    class Meta():
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        ordering = ['id']