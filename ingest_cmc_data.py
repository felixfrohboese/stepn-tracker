import requests
import json
import pandas as pd

import os
from datetime import datetime
import shutil

os.chdir('..')

with open('config.json') as config_file:
    config = json.load(config_file)

cmc_key = config["CMC_KEY"]

os.chdir('./stepn-tracker')

crypto_symbols = {'Solana': 'sol', 'GMT': 'gmt', 'GST': 'gst'}

def get_crypto_prices(symbol, convert='eur'):

    url = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest"
    params = {"symbol": symbol, "convert": convert}
    headers = {"X-CMC_PRO_API_KEY": cmc_key}

    r = requests.get(url, params=params, headers=headers)

    #return r.json()
    return r.json()

for key, value in crypto_symbols.items():

    r1 = get_crypto_prices(symbol=value)

    dateTimeObj = datetime.now()
    year = dateTimeObj.year
    month = dateTimeObj.month
    day = dateTimeObj.day
    hour = dateTimeObj.hour
    minute = dateTimeObj.minute
    second = dateTimeObj.second

    with open(f'{year}-{month}-{day}_{hour}:{minute}:{second}_cmc_data_{value}.json', 'w') as fp:
        json.dump(r1, fp)

    fp.close()

    shutil.move(f'{year}-{month}-{day}_{hour}:{minute}:{second}_cmc_data_{value}.json', \
    f'./JSON_files/{year}-{month}-{day}_{hour}:{minute}:{second}_cmc_data_{value}.json')
