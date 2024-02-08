from django.urls import path
from .views import StockMarketDataListView

urlpatterns = [
    path('', StockMarketDataListView.as_view(), name='index'),

]
