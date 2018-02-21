from django import template

register = template.Library()

@register.filter(name='cutText')
def cutText(value):
    """Removes all values of arg from the given string"""
    return value.split('. ', 1)[0]

@register.filter(name='cutDate')
def cutText(value):
    """Removes all values of arg from the given string"""
    return value.split('T', 1)[0]

