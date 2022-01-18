from xml.dom.minidom import Element
from bs4 import BeautifulSoup
import requests
import time
import re

URL = "https://www.yahoo.co.jp"
webdata = requests.get(URL)
# print(webdata.text)

soup = BeautifulSoup(webdata.text, "html.parser")
# print(soup)
#tabpanelTopics1 > div > div._2jjSS8r_I9Zd6O9NFJtDN- > ul > li:nth-child(1) > article > a > div > div > h1 > span
#tabpanelTopics1 > div > div._2jjSS8r_I9Zd6O9NFJtDN- > ul > li:nth-child(2) > article > a > div > div > h1 > span

# news_list = soup.select("tabpanelTopics1 > div > div._2jjSS8r_I9Zd6O9NFJtDN- > ul > li:nth-child(1) > article > a > div > div > h1")
news_list = soup.find_all("a")
# print(news_list)

element = soup.find_all(href=re.compile("news.yahoo.co.jp/pickup"))
# print(element[0].span.string)
# print(element)
# print(element[0].attrs["href"])

# print(element[1].span.string)
# print(element[1].attrs["href"])

# for news in element:
    # print(news.span.string)
    # print(news.attrs["href"])

pickup_url = [news.attrs["href"] for news in element]
print(pickup_url)

for target_link in pickup_url:
    pickup_data = requests.get(target_link)
    pickup_soup = BeautifulSoup(pickup_data.text, "html.parser")

    pickup_element = pickup_soup.find("p", class_="sc-chYKBT fwErDw")
    # class="sc-bRbqnn iAbiKn"

    targetnews_url = pickup_element.attrs["href"]
    print(targetnews_url)

# uamods-pickup > div.sc-faswKr.dhzAkO > div > p > a