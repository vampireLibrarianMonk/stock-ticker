# Import the admin module from django.contrib, which contains functionalities for Django's admin interface.
from django.contrib import admin

# Import the Stock model from the local models module. This model defines the structure of stock data in the database.
from .models import Stock

# Register the Stock model with the admin site.
# This line of code makes the Stock model accessible through the Django admin interface,
# allowing for the creation, reading, updating, and deletion (CRUD) of Stock records from the admin dashboard.
admin.site.register(Stock)
