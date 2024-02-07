from django.shortcuts import render
import json
from django.core.paginator import Paginator


def home(request):
    with open('./stockview/stock_market_data.json') as f:
        data = json.load(f)

    return render(request, 'stockview/home.html', {'data': data[:10]})
