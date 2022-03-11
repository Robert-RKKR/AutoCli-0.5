# Django Import:
from django import template

# Register template:
register = template.Library()

@register.simple_tag
def verbose_name(provided_object, value):
    return provided_object._meta.get_field(value).verbose_name

@register.simple_tag
def object_attribute_value(provided_object, value):
    return getattr(provided_object, value)
