from django import template
from django.contrib.auth.models import User


register = template.Library()


@register.assignment_tag
def is_exclusive(user):
    usr = User.objects.get(username=user)
    if usr.groups.filter(name="exclusive").exists():
        return True
    else:
        return False
