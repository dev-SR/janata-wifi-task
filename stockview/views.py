from typing import Any
from .models import StockMarketData
from django.views.generic import ListView
from django.shortcuts import render
import json
from django.core.paginator import Paginator


class StockMarketDataListView(ListView):
    model = StockMarketData
    paginate_by = 7

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)

        trade_codes = list(StockMarketData.objects.values_list('trade_code', flat=True).distinct())
        context['trade_codes'] = trade_codes
        return context
