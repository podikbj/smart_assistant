from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField(auto_created=True)
    body = models.TextField(max_length=400)
    image = models.ImageField(upload_to='main/image/')

    def __str__(self):
        return self.title
    class Meta():
        verbose_name = 'Blog'
        verbose_name_plural = 'Blogs'
        ordering = ['pub_date']

