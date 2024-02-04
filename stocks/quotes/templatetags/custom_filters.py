from django import template

register = template.Library()


@register.filter(name='contains_error')
def contains_error(value):
    """Check if the value (string) contains 'error', case-insensitive."""
    return 'error' in value.lower()
