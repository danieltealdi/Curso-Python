from django import template
register = template.Library()
@register.filter()
def precio_tag(value):
    return '{:.2f}€'.format(value)
