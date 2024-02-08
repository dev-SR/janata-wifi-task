from stockview.models import StockMarketData
from pathlib import Path
import json

import os
import random


def run():
    StockMarketData.objects.all().delete()
    ROOT_PATH = Path(os.getcwd())
    JSON_FILE_PATH = ROOT_PATH / 'stockview'/'stock_market_data.json'
    # read
    with open(JSON_FILE_PATH, 'r') as file:
        data = json.load(file)

    # Set seed for reproducibility
    random.seed(69)

    # Select n random samples
    samples = random.sample(data, 1000)

    # Seed the selected samples
    for item in data:
        StockMarketData.objects.create(
            date=item['date'],
            trade_code=item['trade_code'],
            high=item['high'].replace(',', ''),  # remove comma from volume field,
            low=item['low'].replace(',', ''),  # remove comma from volume field,
            open=item['open'].replace(',', ''),  # remove comma from volume field,
            close=item['close'].replace(',', ''),  # remove comma from volume field,
            volume=item['volume'].replace(',', '')  # remove comma from volume field
        )
