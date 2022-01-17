import imp
from bs4 import BeautifulSoup
import requests
import time

URL = "https://www.yahoo.co.jp"
webdata = requests.get(URL)

#tabpanelTopics1 > div > div._2jjSS8r_I9Zd6O9NFJtDN- > ul > li:nth-child(1) > article > a > div > div > h1 > span