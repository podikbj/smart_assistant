from django import template

from .. models import Skill

register = template.Library()

@register.simple_tag()
def get_all_skills():
    return Skill.objects.all()
