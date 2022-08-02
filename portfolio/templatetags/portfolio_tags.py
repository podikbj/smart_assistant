from django import template

from .. models import Skill

register = template.Library()

@register.simple_tag()
def get_my_apps():
    return Skill.objects.all()
