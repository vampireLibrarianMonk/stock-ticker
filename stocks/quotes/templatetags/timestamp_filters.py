from django import template
from datetime import datetime, timezone

register = template.Library()


@register.filter
def milliseconds_to_datetime(value):
    """Convert milliseconds since epoch to datetime."""
    return datetime.fromtimestamp(value / 1000, tz=timezone.utc).strftime('%H:%M %Y-%m-%d')

