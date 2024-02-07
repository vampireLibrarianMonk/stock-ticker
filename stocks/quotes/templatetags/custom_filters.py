# Import the template module from django to create custom template tags and filters.
from django import template

# Create a Library instance, which is necessary for registering custom template tags and filters.
register = template.Library()


# The register.filter decorator is used to register a custom template filter. The 'name' parameter specifies the name
# to be used for this filter in templates, which is 'contains_error' in this case.
@register.filter(name='contains_error')
# Define the filter function that takes 'value' as its argument.
# This 'value' is expected to be a string that will be checked for the presence of 'error'.
def contains_error(value):
    """Check if the value (string) contains 'error', case-insensitive."""
    # Convert the value to lowercase and check if 'error' is a substring of value.
    # The use of .lower() ensures that the check is case-insensitive.
    return 'error' in value.lower()
