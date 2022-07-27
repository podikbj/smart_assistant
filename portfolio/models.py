from django.db import models
from django.urls import reverse

class Portfolio(models.Model):
    title = models.CharField(max_length=255, default = "Python")
    summary = models.TextField(max_length=400)
    skill = models.ForeignKey('Skill', on_delete=models.PROTECT, blank=True, null=True)
    created_on = models.DateField(auto_now_add=True, blank=True, null=True)
    votes = models.IntegerField(default=0)

    # url = models.URLField(max_length=255, unique=True, db_index=True, verbose_name='url', null=True)

    def get_absolute_url(self):
        return f'/portfolio/{self.id}'

    def __str__(self):
        return self.title
    class Meta():
        verbose_name = 'Link to a certain project'
        verbose_name_plural = 'Links to a certain projects'
        ordering = ['skill_id']

class Skill(models.Model):
    title = models.CharField(max_length=100, db_index=True, verbose_name='skill')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('skill', kwargs={'skill_id': self.pk})

    class Meta():
        verbose_name = 'Skill'
        verbose_name_plural = 'Skills'
        ordering = ['id']