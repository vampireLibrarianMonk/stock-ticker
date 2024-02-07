# Import the forms module from django to create form classes
from django import forms

# Import the Stock model from the models module in the same application
from .models import Stock


# Define the StockForm class, which inherits from forms.ModelForm.
# ModelForm is a convenient way to create a Django form based on a model.
class StockForm(forms.ModelForm):
    # Meta class is used to provide metadata to the StockForm class. This inner class tells Django about the model
    # (Stock) the form is associated with and which fields should be included in the form.
    class Meta:
        # Specify the model that this form is linked to, which is the Stock model.
        # The form will be used to create or update Stock instances.
        model = Stock
        # Specify the fields that should be included in the form.
        # In this case, only the 'ticker' field of the Stock model is included.
        # This makes the form a single-field form for entering or editing a stock's ticker symbol.
        fields = ['ticker']
