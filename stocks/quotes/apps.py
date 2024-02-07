# Import the AppConfig class from django.apps, which is necessary for configuring applications in Django.
from django.apps import AppConfig


# Define the QuotesConfig class, which inherits from AppConfig. AppConfig classes are used to configure some of the
# application-specific settings such as the application name, and model field defaults.
class QuotesConfig(AppConfig):
    # Specify the default type of auto field to use for primary keys in models.
    # 'django.db.models.BigAutoField' is a type of field that automatically increments.
    # It is suitable for primary keys and is capable of storing very large integers.
    # This is useful when you expect a very large number of objects to be created in the database.
    default_auto_field = 'django.db.models.BigAutoField'

    # The name attribute specifies the full Python path to the application. Django uses this configuration to locate
    # and register the application. In this case, 'quotes' indicates that the application is defined in a module (or
    # package) named quotes. This name is used by Django in various internal mechanisms, such as when linking models
    # to their respective applications.
    name = 'quotes'
