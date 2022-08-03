from django import template

from .. models import Cities

register = template.Library()

@register.simple_tag()
def get_all_cities():
    return Cities.objects.all()