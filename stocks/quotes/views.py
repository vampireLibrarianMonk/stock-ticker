# Django's messaging framework for displaying temporary messages to the user.
from django.contrib import messages

# render for combining templates with context, and redirect for URL redirections.
from django.shortcuts import render, redirect

# stockForm from forms to handle user input in a structured and secure manner.
from .forms import StockForm

# loads function from json module as json_loads for parsing JSON strings into Python dictionaries.
from json import loads as json_loads

# JSONDecodeError for handling exceptions when parsing JSON fails.
from json.decoder import JSONDecodeError

# Stock model to represent stock data within the database.
from .models import Stock

# getenv from os module to securely access environment variables.
from os import getenv

# requests library for making HTTP requests to web services or APIs.
import requests

# IEX Cloud Secret Token and API URL for current Data Bundle
secret_token = getenv('SECRET_TOKEN')
iex_cloud_url = 'https://api.iex.cloud/v1/data/core/iex_tops/'


# Home Page
def home(request):
    # Handle HTTP GET and POST requests to the home page.
    if request.method == 'POST':
        # Retrieve ticker symbol from POST request form data.
        ticker_symbol = request.POST['ticker']

        # Check if ticker symbol field is empty and return home page if true.
        if ticker_symbol == '':
            return render(request, 'home.html', {})
        else:
            # Make an API request to a stock information service using the ticker symbol.
            api_request = requests.get(f'{iex_cloud_url}{ticker_symbol}?token={secret_token}')

            # Check if the API request returns an empty JSON array, indicating no data found.
            if api_request.content == b'[]':
                # Display an error message if no data is returned for the valid ticker symbol.
                messages.error(request, f"{ticker_symbol} is valid but returned no data. "
                                        f"Please check the ticker symbol.")
                return render(request, 'home.html', {})
            else:
                try:
                    # Attempt to load the API response content as JSON.
                    api_return = json_loads(api_request.content)
                    # Display a success message if the ticker symbol is found and data is returned.
                    messages.success(request, f"{ticker_symbol} found!")
                except JSONDecodeError as error:
                    # Catch JSON decoding errors and display an error message.
                    messages.error(request, error)
                    return render(request, 'home.html', {})
                except Exception as exception:
                    # Catch all other exceptions and display an error message.
                    messages.error(request, exception)
                    return render(request, 'home.html', {})

                # Render the home page template with the API data if successful.
                return render(request, 'home.html', {'api_return': api_return})
    else:
        # Render the home page template for GET requests with no form data.
        return render(request, 'home.html', {})


# About Informational Page
def about(request):
    return render(request, 'about.html', {})


# Add Stock Functionality
def add_stock(request):
    # Checks if the request is a POST request indicating form submission.
    if request.method == 'POST':
        # Instantiates a StockForm with data from the request.
        form = StockForm(request.POST)

        # Validates the form data.
        if form.is_valid():
            # Extracts the ticker symbol from the validated form data.
            ticker_symbol = form.cleaned_data["ticker"]

            # Constructs the API URL to verify the ticker symbol using the IEX Cloud API.
            api_url = f'{iex_cloud_url}{ticker_symbol}?token={secret_token}'
            response = requests.get(api_url)

            # Checks if the API call was successful (HTTP status code 200).
            if response.status_code == 200:
                # Parses the API response data.
                stock_data = response.json()
                if stock_data:  # Checks if the API response contains data.
                    # Saves the form data to the database if the ticker symbol is valid and data is returned.
                    new_stock = form.save()
                    # Notifies the user that the stock has been successfully added.
                    messages.success(request, "Stock Has Been Added!")
                    # Redirects to the portfolio management page.
                    return redirect('portfolio_management')
                else:
                    # Notifies the user if the ticker symbol is valid but no data was returned.
                    messages.error(request,
                                   f"{ticker_symbol} is valid but returned no data. Please check the ticker symbol.")
            else:
                # Notifies the user if the ticker symbol is invalid.
                messages.error(request, "Invalid ticker symbol. Please check input and try again.")
        else:
            # Notifies the user if there was an error adding the stock due to invalid form data.
            messages.error(request, "Error Adding Stock. Please check input.")

    else:
        # Creates a new, empty StockForm instance for a GET request.
        form = StockForm()

    # Retrieves all ticker symbols from the database.
    ticker = Stock.objects.all()
    output = []

    # Iterates through each ticker symbol to fetch and append its data to the output list.
    for ticker_item in ticker:
        api_url = f'{iex_cloud_url}{ticker_item.ticker}?token={secret_token}'
        try:
            response = requests.get(api_url)
            if response.status_code == 200:
                # Appends the API response data to the output list if successful.
                stock_data = response.json()
                output.append(stock_data)
            else:
                # Notifies the user if fetching data for a ticker symbol failed.
                messages.error(request, f"Failed to fetch data for {ticker_item.ticker}.")
        except Exception as e:
            # Handles any exceptions during the API call and notifies the user.
            messages.error(request, f"An error occurred while fetching data for {ticker_item.ticker}: {str(e)}")

    # Additional handling for form errors, specifically targeting the 'ticker' field.
    if len(form.errors) > 0:
        # Extracts errors related to the 'ticker' field.
        error_list = form.errors.as_data().get('ticker', [])

        errors = [str(e) for error in error_list for e in error]
        if errors:
            # Joins and displays errors related to the 'ticker' field.
            messages.error(request, "\n".join(errors))

    # Renders the portfolio management template with the form, ticker symbols, and their data.
    return render(request, 'portfolio_management.html', {'form': form, 'ticker': ticker, 'output': output})


# Delete Stock with ID Functionality
def delete_stock_with_id(request, stock_id):
    # Retrieve the Stock object by its primary key (stock_id) from the database.
    # The Stock model is assumed to be defined elsewhere in the project,
    # representing the stock entities in the database.
    item = Stock.objects.get(pk=stock_id)

    # Delete the retrieved Stock object from the database.
    # This operation will remove the specific stock identified by stock_id from the database.
    item.delete()

    # Display a success message to the user indicating that the stock has been deleted.
    # The messages framework is used to queue up a message to be shown to the user on the next page load.
    messages.success(request, "Stock Has Been Deleted!")

    # Redirect the user to the 'portfolio_management' page after the delete operation.
    # The 'redirect' function is used to navigate the user to a different page, in this case, the portfolio management
    # page, which is identified by the name 'portfolio_management' in the project's URL configuration.
    return redirect('portfolio_management')


# Portfolio Management Functionality
def portfolio_management(request):
    # Create an instance of StockForm. This form is used to add new stocks.
    # The form is populated with data from POST request if available, otherwise an empty form is created.
    form = StockForm(request.POST or None)

    # Check if the request method is POST, indicating form submission.
    if request.method == 'POST':
        # Validate the form data. This checks whether the submitted data is valid according to the form fields defined
        # in StockForm.
        if form.is_valid():
            # Save the new stock data to the database. This step creates or updates the stock record.
            form.save()
            # Display a success message to the user indicating that the stock has been added.
            messages.success(request, "Stock Has Been Added!")
            # Redirect to the same page (portfolio management page) to refresh and show the updated list including the
            # new stock.
            return redirect('portfolio_management')

    # Retrieve all stock objects from the database to display them on the portfolio management page.
    ticker = Stock.objects.all()
    output = []  # Initialize an empty list to store the API response data for each stock.

    # Loop through each stock object retrieved from the database.
    for ticker_item in ticker:
        try:
            # Make an API request to fetch detailed data for the current stock ticker.
            # The request URL is constructed dynamically using the stock's ticker symbol, IEX Cloud URL, and a secret
            # token for authentication.
            api_request = requests.get(f'{iex_cloud_url}{ticker_item.ticker}?token={secret_token}')
            # Parse the API response and assume it returns a list. Get the first item from the list as the API return.
            api_return = json_loads(api_request.content)[0]
            # Append the API response data for the current stock to the output list.
            output.append(api_return)
        except Exception as e:
            # If an error occurs during the API request, display an error message specifying the ticker symbol and the
            # error message.
            messages.error(request, f"Error fetching data for {ticker_item.ticker}: {str(e)}")

    # Render the portfolio management page with the context data.
    # The context includes the stock form, all stock objects, and the API response data for each stock.
    return render(request, 'portfolio_management.html',
                  {'form': form, 'ticker': ticker, 'output': output})
