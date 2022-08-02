import os


from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

cmckey = os.environ.get('CMC_KEY')
pw = os.environ["CMC_KEY"]

print(cmckey, pw)
