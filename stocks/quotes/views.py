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
    import requests
    import json

    if request.method == 'POST':
        form = StockForm(request.POST or None)

        if form.is_valid():
            form.save()
            messages.success(request, "Stock Has Been Added!")
            return redirect('add_stock')
    else:
        ticker = Stock.objects.all()
        output = []
        for ticker_item in ticker:
            api_request = requests.get(
                f'{iex_cloud_url}{str(ticker_item)}?token={secret_token}')

            try:
                api_return = json.loads(api_request.content)[0]
                print(api_return)
                output.append(api_return)
            except Exception as e:
                api_return = "Error..."

        return render(request, 'add_stock.html', {'ticker': ticker, 'output': output})


def delete(request, stock_id):
    item = Stock.objects.get(pk=stock_id)
    item.delete()
    messages.success(request, "Stock Has Been Deleted!")
    return redirect(delete_stock)


def delete_stock(request):
    ticker = Stock.objects.all()
    return render(request, 'delete_stock.html', {'ticker': ticker})
