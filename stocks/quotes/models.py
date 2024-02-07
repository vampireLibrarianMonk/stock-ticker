# Import the models module from django.db to define model classes
from django.db import models


# Define the Stock model class, which inherits from models.Model
class Stock(models.Model):
    # Define a CharField for the ticker symbol of the stock. This field is limited to a maximum of 5 characters
    # and is set to be unique, meaning each stock in the database must have a distinct ticker symbol.
    # See About page for specific on ticker symbols in each exchange
    ticker = models.CharField(max_length=5, unique=True)

    # Define the __str__ method, which is a special method used to return a string representation of the object.
    # When you call str() on an instance of Stock, or when Django needs to display a Stock object in the admin,
    # this method returns the ticker symbol of the Stock.
    def __str__(self):
        return self.ticker
