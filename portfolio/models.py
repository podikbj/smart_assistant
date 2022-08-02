from django.db import models
from django.urls import reverse

class Portfolio(models.Model):
    title = models.CharField(max_length=255, default = "Python")
    summary = models.TextField(max_length=400)
    skill = models.ForeignKey('Skill', on_delete=models.PROTECT, blank=True, null=True)
    created_on = models.DateField(auto_now_add=True, blank=True, null=True)
    slug = models.SlugField(max_length=100, unique=True, db_index=True, verbose_name="slug", null=True)
    votes = models.IntegerField(default=0)


    def get_absolute_url(self):
        return reverse('project_detail', kwargs={'project_slug': self.slug})

    def __str__(self):
        return self.title
    class Meta():
        verbose_name = 'Link to a certain project'
        verbose_name_plural = 'Links to a certain projects'
        ordering = ['skill_id']

class Skill(models.Model):
    title = models.CharField(max_length=100, db_index=True, verbose_name='skill')
    image = models.ImageField(null=True, verbose_name='skill_icon')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="slug", null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('display_projects_by_skill', kwargs={'skill_slug':self.slug})


    class Meta():
        verbose_name = 'Skill'
        verbose_name_plural = 'Skills'
        ordering = ['id']