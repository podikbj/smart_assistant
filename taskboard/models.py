from django.db import models
from django.urls import reverse

class Task(models.Model):
    context = models.TextField(max_length=300, verbose_name='Task')
    created_on = models.DateTimeField('Date', auto_now_add=True)
    deadline_day = models.DateField('Deadline_day', null=True)
    deadline_time = models.TimeField('Deadline_time', null=True)

    def __str__(self):
        return self.context

    def get_absolute_url(self):
        return reverse('task_details', kwargs={'pk': self.pk})

    class Meta():
        verbose_name = 'Task'
        verbose_name_plural = 'Tasks'
        ordering = ['deadline_day', 'deadline_time']

