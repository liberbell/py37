from bs4 import BeautifulSoup
import requests
import time

URL = "https://www.yahoo.co.jp"
webdata = requests.get(URL)
# print(webdata.text)

soup = BeautifulSoup(webdata.text, "html.parser")
print(soup)
#tabpanelTopics1 > div > div._2jjSS8r_I9Zd6O9NFJtDN- > ul > li:nth-child(1) > article > a > div > div > h1 > span
#tabpanelTopics1 > div > div._2jjSS8r_I9Zd6O9NFJtDN- > ul > li:nth-child(2) > article > a > div > div > h1 > span

# news_list = soup.select("tabpanelTopics1 > div > div._2jjSS8r_I9Zd6O9NFJtDN- > ul > li:nth-child(1) > article > a > div > div > h1")
news_list = soup.find_all("span")
print(news_list[0])