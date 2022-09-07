import threading
import time
import requests

import iso8601
from datetime import datetime

from exchange.models import Gold, Silver
from exchange.utils import oz_to_g, oz_to_kg

gold_price_url = "https://api.monex.com:444/api/v1/Metals/spot/current?metals=GBXSPOT"
silver_price_url = "https://api.monex.com:444/api/v1/Metals/spot/current?metals=SBSPOT"

hkd_rub_url = "https://www.investing.com/currencies/hkd-rub"


def get_data():
    # params = dict(
    #     origin='Chicago,IL',
    #     destination='Los+Angeles,CA',
    #     waypoints='Joplin,MO|Oklahoma+City,OK',
    #     sensor='false'
    # )

    # resp = requests.get(url=url, params=params)
    resp_gold = requests.get(url=gold_price_url)
    json_gold = resp_gold.json()  # Check the JSON Response Content documentation

    resp_silver = requests.get(url=silver_price_url)
    json_silver = resp_silver.json()  # Check the JSON Response Content documentation

    gold = transform_data(json_gold)
    silver = transform_data(json_silver)

    Gold.objects.create(**gold)
    Silver.objects.create(**silver)

    resp_currency = requests.get(url=hkd_rub_url)
    json_currency = resp_currency.json()


params = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
          'Accept-Encoding': 'gzip, deflate, br',
          'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3',
          'Connection': 'keep-alive',
          'Host': 'www.xe.com',
          'Sec-Fetch-Dest': 'document',
          'Sec-Fetch-Mode': 'navigate',
          'Sec-Fetch-Site': 'none',
          'Sec-Fetch-User': '?1',
          'Upgrade-Insecure-Requests': '1',
          'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:104.0) Gecko/20100101 Firefox/104.0'}


def transform_data(json):
    input = json['data'][0]

    output = {
        'last': float(input['last']),
        'bid': float(input['bid']),
        'ask': float(input['ask']),
        'high': float(input['high']),
        'low': float(input['low']),
        'open': float(input['open']),
        'previousClose': float(input['previousClose']),
        'timestamp': iso8601.parse_date(input['timestamp']),

        'price_g': oz_to_g(input['last']),
        'price_kg': oz_to_kg(input['last']),
        'previousClose_g': oz_to_g(input['previousClose']),
        'previousClose_kg': oz_to_kg(input['previousClose']),
    }

    return output


def start_evaluation():
    t = threading.Thread(target=evaluate_positions)
    t.setDaemon(True)
    t.start()

    return True


def evaluate_positions():
    while True:
        time.sleep(10)
