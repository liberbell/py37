import pandas as pd
import requests
from datetime import datetime as dt

URL = "https://finance.yahoo.com/quote/AAPL/history?p=AAPL"
# webdata = pd.read_html(URL, header=0)
webdata = pd.read_html(requests.get(URL, headers={'User-agent': 'Mozilla/5.0'}).text,header=0)

# print(webdata[0].head())
print(webdata[0].tail())

webdata[0]["Adj Close**"] = pd.to_numeric(webdata[0]["Adj Close**"], errors="coerce")
print(webdata[0].tail())

webdata[0].dropna(inplace=True)
print(webdata[0].tail())

webdata[0]["Date2"] = [dt.strptime(i, "%b %d, %Y") for i in webdata[0]["Date"]]
