from django.db import models

class Weather(models.Model):
    city_name = models.CharField(max_length=100)

    def __str__(self):
        return self.city_name

    class Meta():
        verbose_name = 'City name'
        verbose_name_plural = 'Cities names'
