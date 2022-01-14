import pandas as pd
import requests

URL = "https://finance.yahoo.com/quote/AAPL/history?p=AAPL"
# webdata = pd.read_html(URL, header=0)
webdata = pd.read_html(requests.get(URL, headers={'User-agent': 'Mozilla/5.0'}).text,header=0)

print(webdata[0].head())
print(webdata[0].tail())