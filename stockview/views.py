from django.shortcuts import render
import json
from django.core.paginator import Paginator


def home(request):
    with open('./stockview/stock_market_data.json') as f:
        data = json.load(f)

    paginator = Paginator(data, 10)  # Show 10 items per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'stockview/home.html', {'page_obj': page_obj})
