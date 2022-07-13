from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse


class Links(models.Model):
    title = models.CharField(max_length=33, verbose_name='title')
    category = models.ForeignKey('Categories', on_delete=models.PROTECT)
    sub_category = models.CharField(max_length=50, verbose_name='subcategory')
    url = models.URLField(max_length=255, unique=True, db_index=True, verbose_name='url', null=True)
    context = models.TextField(max_length=300, verbose_name='context')
    created_on = models.DateTimeField('Date', auto_now_add=True)

    def get_absolute_url(self):
        return f'/links/{self.id}'

    # def save(self, *args, **kwargs):
    #     if not self.slug:
    #         self.slug = slugify(self.title)
    #     super(Links, self).save(*args, **kwargs)

    def __str__(self):
        return self.title
    class Meta():
        verbose_name = 'Link to a certain website'
        verbose_name_plural = 'Links to a certain websites'
        ordering = ['sub_category', 'title']


class Categories(models.Model):
    title = models.CharField(max_length=100, db_index=True, verbose_name='title')
    created_on = models.DateTimeField('Date', auto_now_add=True)

    def __str__(self):
        return self.title
    def get_absolute_url(self):
        # return reverse('category', kwargs={'category_id': self.pk})
        return f'/links/category/{self.id}'

    class Meta():
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        ordering = ['id']

