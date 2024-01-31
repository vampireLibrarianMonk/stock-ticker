from django.shortcuts import render, redirect
from .models import Stock
from .forms import StockForm
from django.contrib import messages


def home(request):
    import requests
    import json

    if request.method == 'POST':
        ticker = request.POST['ticker']

        # pk_95de9948c2164d88a23069febccef664
        api_request = requests.get(
            f'https://api.iex.cloud/v1/data/core/quote/{ticker}?token=sk_17a74334b7a54247b523922687d38e56')

        try:
            api_list = json.loads(api_request.content)
        except Exception as e:
            api_list = "Error..."

        return render(request, 'home.html', {'api_list': api_list})

    else:
        return render(request, 'home.html', {'ticker': "Enter a Ticker Symbol Above..."})


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
                f'https://api.iex.cloud/v1/data/core/quote/{str(ticker_item)}?token=sk_17a74334b7a54247b523922687d38e56')

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