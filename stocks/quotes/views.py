from django.shortcuts import render, redirect
from .models import Stock
from .forms import StockForm
from django.contrib import messages
from os import getenv
from json.decoder import JSONDecodeError
import requests
import json

secret_token = getenv('SECRET_TOKEN')
iex_cloud_url = 'https://api.iex.cloud/v1/data/core/iex_tops/'


def home(request):
    if request.method == 'POST':
        ticker = request.POST['ticker']

        # Assuming iex_cloud_url, ticker, and secret_token are defined earlier
        api_request = requests.get(f'{iex_cloud_url}{ticker}?token={secret_token}')

        # Check for empty JSON array
        if api_request.content == b'[]':
            api_return = "Error: No data available for the given ticker."
        else:
            try:
                api_return = json.loads(api_request.content)
            except JSONDecodeError:
                # If JSON decoding fails, return the raw content as a UTF-8 decoded string
                api_return = "Error: " + api_request.content.decode('utf-8')
            except Exception as e:
                # Generic exception handling as a fallback
                api_return = f"Unexpected Error: {str(e)}"

        return render(request, 'home.html', {'api_return': api_return})

    else:

        return render(request, 'home.html', {})


def about(request):
    return render(request, 'about.html', {})


def add_stock(request):
    if request.method == 'POST':
        form = StockForm(request.POST)

        if form.is_valid():
            # Extract ticker symbol from form data
            ticker_symbol = request.POST["ticker"]

            # Verify ticker symbol with an API call before saving
            api_url = f'{iex_cloud_url}{ticker_symbol}?token={secret_token}'
            response = requests.get(api_url)
            if response.status_code == 200:
                # Assuming a successful response means a valid ticker
                stock_data = response.json()
                if stock_data:  # Check if the API returned data
                    new_stock = form.save()
                    messages.success(request, "Stock Has Been Added!")
                    return redirect('portfolio_management')
                else:
                    # API returned a successful status code but no data
                    messages.error(request,
                                   f"{ticker_symbol} is valid but returned no data. "
                                   "Please check the ticker symbol.")
            else:
                # API call failed - likely an invalid ticker symbol
                messages.error(request, "Invalid ticker symbol. Please check input and try again.")
        else:
            messages.error(request, "Error Adding Stock. Please check input.")

    else:
        form = StockForm()  # Create a new form to display

    ticker = Stock.objects.all()
    output = []

    for ticker_item in ticker:
        api_url = f'{iex_cloud_url}{ticker_item.ticker}?token={secret_token}'
        try:
            response = requests.get(api_url)
            if response.status_code == 200:
                stock_data = response.json()
                output.append(stock_data)
            else:
                messages.error(request, f"Failed to fetch data for {ticker_item.ticker}.")
        except Exception as e:
            messages.error(request, f"An error occurred while fetching data for {ticker_item.ticker}: {str(e)}")

    if len(form.errors) > 0:
        error_list = form.errors['ticker'].data[0].error_list

        if len(error_list) > 0:

            errors = []

            for message_list in error_list:
                for message in message_list:
                    errors.append(message)

            messages.error(request, "\n".join(errors))

    return render(request, 'portfolio_management.html', {'form': form, 'ticker': ticker, 'output': output})


# Updated delete_stock view that doesn't expect any arguments
def delete_stock(request):
    ticker = Stock.objects.all()
    return render(request, 'delete_stock.html', {'ticker': ticker})


# New view to handle delete_stock with stock_id
def delete_stock_with_id(request, stock_id):
    item = Stock.objects.get(pk=stock_id)
    item.delete()
    messages.success(request, "Stock Has Been Deleted!")
    return redirect('portfolio_management')


def portfolio_management(request):
    form = StockForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, "Stock Has Been Added!")
            return redirect('portfolio_management')  # Redirect to the same page to refresh

    ticker = Stock.objects.all()
    output = []

    for ticker_item in ticker:
        try:
            api_request = requests.get(f'{iex_cloud_url}{ticker_item.ticker}?token={secret_token}')
            api_return = json.loads(api_request.content)[0]  # Assuming the API returns a list
            output.append(api_return)
        except Exception as e:
            messages.error(request, f"Error fetching data for {ticker_item.ticker}: {str(e)}")

    return render(request, 'portfolio_management.html', {'form': form, 'ticker': ticker, 'output': output})
