# Import the template module from django to create custom template tags and filters.
from django import template

# Import the datetime and timezone classes from the datetime module for handling date and time.
from datetime import datetime, timezone

# Create a Library instance, which is necessary for registering custom template tags and filters.
register = template.Library()


# The register.filter decorator is used to register a custom template filter.
# In this case, we're defining a filter named 'milliseconds_to_datetime'.
@register.filter
# Define the filter function that takes a value as its argument.
# This value represents the number of milliseconds since the Unix epoch (January 1, 1970).
def milliseconds_to_datetime(value):
    """Convert milliseconds since epoch to datetime."""
    # Convert milliseconds to seconds by dividing by 1000, then use datetime.fromtimestamp
    # to convert the seconds to a datetime object. Specify timezone.utc to set the timezone to UTC.
    # The strftime method is used to format the datetime object into a string according to the given format.
    return datetime.fromtimestamp(value / 1000, tz=timezone.utc).strftime('%H:%M %Y-%m-%d')
