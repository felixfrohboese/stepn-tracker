from sqlalchemy import create_engine
from sqlalchemy import inspect
from sqlalchemy.orm import sessionmaker

import os
import json
import shutil

os.chdir('..')

with open('config.json') as config_file:
    config = json.load(config_file)

user_name = config.get("admin_user")
password = config.get("admin_password")
host = config.get("host")
database_name = config.get("database_name")
port_number = config.get("port_number")

os.chdir('./stepn-tracker')

#setup_engine = f"postgresql://{user_name}:{password}@{host}:{port_number}/{database_name}"
setup_engine = f"postgresql://postgres:xvfD4bDDxswy@127.0.0.1:5432/stepn-tracker-db"


engine = create_engine(setup_engine)
#inspector = inspect(engine)
#schemas = inspector.get_schema_names()

sql_statement = 'CREATE TABLE IF NOT EXISTS records (id SERIAL  PRIMARY KEY, timestamp TIMESTAMP DEFAULT now(), name VARCHAR, symbol VARCHAR, price REAL)'
engine.execute(sql_statement)

fileList = []
for filenames in os.walk('./JSON_files'):
    fileList.append(filenames)
pure_list = fileList[0][2]

for i in pure_list:
    if i.split('.')[1] != "json":
        pure_list.remove(i)

done_indices = []

os.chdir('./JSON_files')

for no, i in enumerate(pure_list):

    with open(i) as json_file:
        api_data = json.load(json_file)

    sym0 = i.split('_')[-1]
    sym = sym0.split('.')[0]

    #api_data = get_crypto_prices(sym)
    symbol_upper = sym.upper()

    price = round(api_data['data'][f'{symbol_upper}']['quote']['EUR']['price'], 2)
    name = api_data['data'][f'{symbol_upper}']['name']
    symbol = api_data['data'][f'{symbol_upper}']['symbol']

    sql_statement_insert = f"INSERT INTO records (name, symbol, price) VALUES ('{name}', '{symbol}', {price})"
    engine.execute(sql_statement_insert)

    done_indices.append(no)

os.chdir('..')

for i in done_indices:
    shutil.move(f'./JSON_files/{pure_list[i]}', f'./JSON_files_done/{pure_list[i]}')
