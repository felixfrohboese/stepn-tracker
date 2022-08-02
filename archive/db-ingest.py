
from sqlalchemy import create_engine
from sqlalchemy import inspect
from sqlalchemy.orm import sessionmaker

import requests
import json
import pandas as pd

import os

cmckey = os.environ["X-CMC_PRO_API_KEY"]

# Establishing the connection
user_name = "postgres"
#pw = os.environ["POSTGRES_PAT"]
host = "127.0.0.1"
database_name = "cmcdata2"
port_number = "5432"

# create engine and data base objects
setup_engine = f"postgres://{user_name}@{host}:{port_number}/{database_name}"
engine = create_engine(setup_engine)
inspector = inspect(engine)
schemas = inspector.get_schema_names()

# **CoinMarketCap API**

crypto_symbols = {'Bitcoin': 'btc', 'Ethereum': 'eth', 'Ripple': 'xrp', 'DeFiChain': 'dfi', 'Decentraland': 'mana', 'Enjin': 'enj', 'Wax Protocol': 'waxp'}

def get_crypto_prices(symbol, convert='eur'):

    url = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest"
    params = {"symbol": symbol, "convert": convert}
    headers = {"X-CMC_PRO_API_KEY": cmckey}

    r = requests.get(url, params=params, headers=headers)

    return r.json()

coin_prices = {}

for coin, symbol in crypto_symbols.items():

    api_data = get_crypto_prices(symbol)
    symbol_upper = symbol.upper()
    price = api_data['data'][f'{symbol_upper}']['quote']['EUR']['price']

    coin_prices.update({coin: price})

#coin_prices











def execute_print_query(sql_statement):
    """
    Returns the query formatted as a Pandas' dataframe.

    Parameters
    -----------
    sql_statement : string
        The string containing the desired SQL statement to run.

    Returns
    --------
    pandas.DataFrame
    """

    query = engine.execute(sql_statement)
    return pd.DataFrame(query.fetchall(), columns=query.keys())
