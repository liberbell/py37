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
# print(pickup_url)

for target_link in pickup_url:
    pickup_data = requests.get(target_link)
    pickup_soup = BeautifulSoup(pickup_data.text, "html.parser")

    pickup_element = pickup_soup.find("p", class_="sc-chYKBT fwErDw")
    # class="sc-bRbqnn iAbiKn"

    targetnews_url = pickup_element.a.attrs["href"]
    # print(targetnews_url)

    news_data = requests.get(targetnews_url)
    news_soap = BeautifulSoup(news_data.text, "html.parser")

    print(news_soap.title.text)
    print(targetnews_url)
    
    detail_text = news_soap.find(class_=re.compile("SlinkDirectlink"))
    print(detail_text.text if hasattr(detail_text, "text") else "", end="\n\n")

    time.sleep(1)

# uamods-pickup > div.sc-faswKr.dhzAkO > div > p > a
# <p class="sc-hmXxxW fDHxNM yjSlinkDirectlink highLightSearchTarget">　政府が<a class="yjSlinkDirectlinkHl" data-query="新型コロナウイルス" rel="noopener" href="https://search.yahoo.co.jp/search?ei=UTF-8&amp;rkf=1&amp;slfr=1&amp;qrw=0&amp;p=%E6%96%B0%E5%9E%8B%E3%82%B3%E3%83%AD%E3%83%8A%E3%82%A6%E3%82%A4%E3%83%AB%E3%82%B9&amp;fr=link_kw_nws_direct" target="_blank" style="cursor: pointer;">新型コロナウイルス</a>の「<a class="yjSlinkDirectlinkHl" data-query="まん延防止等重点措置" rel="noopener" href="https://search.yahoo.co.jp/search?ei=UTF-8&amp;rkf=1&amp;slfr=1&amp;qrw=0&amp;p=%E3%81%BE%E3%82%93%E5%BB%B6%E9%98%B2%E6%AD%A2%E7%AD%89%E9%87%8D%E7%82%B9%E6%8E%AA%E7%BD%AE&amp;fr=link_kw_nws_direct" target="_blank" style="cursor: pointer;">まん延防止等重点措置</a>」を1都10県で適用する方向となったのを受け、各自治体は18日、対象地域の範囲や飲食店の営業時間短縮など具体的な措置内容の調整を本格化させた。感染力の強い新変異株「オミクロン株」が急速に広がる中で医療<a class="yjSlinkDirectlinkHl" data-query="逼迫" rel="noopener" href="https://search.yahoo.co.jp/search?ei=UTF-8&amp;rkf=1&amp;slfr=1&amp;qrw=0&amp;p=%E9%80%BC%E8%BF%AB&amp;fr=link_kw_nws_direct" target="_blank" style="cursor: pointer;">逼迫</a>の回避と経済活動の維持の両立を模索。19日にも予定される正式決定までの間、難しい検討を迫られそうだ。

# <a href="https://www.47news.jp/relation/2022011804" data-ylk="rsec:related;slk:photo;pos:1;view_pos:1;shcid:bd0df445ca7d4215f80b59b4a85299b7f3634036;url:https%3A%2F%2Fwww.47news.jp%2Frelation%2F2022011804;title:【写真】ワクチンパッケージ、一時停止へ;" data-rapid_p="41">【写真】ワクチンパッケージ、一時停止へ</a></p>