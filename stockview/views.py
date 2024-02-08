from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from typing import Any
from .models import StockMarketData
from django.views.generic import ListView
from django.shortcuts import render
from django.core.paginator import Paginator
import plotly.express as px
import plotly.graph_objs as go


class StockMarketDataListView(ListView):
    model = StockMarketData
    paginate_by = 7

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        # Get unique trade codes for autocomplete
        trade_codes = list(StockMarketData.objects.values_list('trade_code', flat=True).distinct())
        context['trade_codes'] = trade_codes

        trade_code = self.request.GET.get('trade_code')
        data = StockMarketData.objects.filter(trade_code=trade_code).order_by(
            'date') if trade_code else StockMarketData.objects.all().order_by('date')

        # Convert queryset values to lists
        dates = list(data.values_list('date', flat=True))
        close_prices = list(data.values_list('close', flat=True))
        volumes = list(data.values_list('volume', flat=True))

        # Create figure for multi-axis chart
        fig = go.Figure()

        # Add trace for close price
        fig.add_trace(go.Scatter(x=dates,
                                 y=close_prices,
                                 mode='lines',
                                 name='Close Price'))

        # Add trace for volume
        fig.add_trace(go.Bar(x=dates,
                             y=volumes,
                             yaxis='y2',
                             name='Volume'))

        # Set layout
        fig.update_layout(title='Stock Market Data',
                          xaxis=dict(title='Date'),
                          yaxis=dict(title='Close Price', side='left', position=0.05),
                          yaxis2=dict(title='Volume', side='right', overlaying='y', position=0.95),
                          autosize=True,  # Set autosize to True to allow the chart to take full width
                          width=900,  # Set a default width to avoid chart shrinking
                          height=500)  # Set a default height

        # Serialize figure to HTML and add t context
        context['chart_html'] = fig.to_html()

        return context


class StockMarketDataCreateView(CreateView):
    model = StockMarketData
    fields = ['date', 'trade_code', 'high', 'low', 'open', 'close', 'volume']
    success_url = reverse_lazy('index')


class StockMarketDataUpdateView(UpdateView):
    model = StockMarketData
    fields = ['date', 'trade_code', 'high', 'low', 'open', 'close', 'volume']
    success_url = reverse_lazy('index')


class StockMarketDataDeleteView(DeleteView):
    model = StockMarketData
    success_url = reverse_lazy('index')
