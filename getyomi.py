import requests
from bs4 import BeautifulSoup

URL = "https://www.yomiuri.co.jp/"
webdata = requests.get(URL)

if webdata.status_code != 200:
    print("Something wrong.")

# print(webdata.text)

soup = BeautifulSoup(webdata.text, "html.parser")
# print(soup)
# body > div.home-2021-primary > div.home-2021-primary__main > div.headline > article:nth-child(1) > div > h3 > a

element = soup.select("div.headline > article:nth-child(1) > div > h3 > a")
print(element[0])
print(element[0].contents[0])
print(element[0].attrs["href"])
print("------")

element = soup.select("div.headline")
# print(element[0].prettify)
# print(element[0].h3.a.string)
# print(element[0].h3.a["href"])

# print(element[0].article.next_sibling.next_sibling.h3.a.string)
# print(element[0].article.next_sibling.next_sibling.h3.a["href"])

# for sib in element[0].article.next_sibling:
#     print(sib.h3.a.string if sib != "\n" else "")
#     print(sib.h3.a["href"])

# print(element[0].prettify)

elms_news = element[0].find_all("h3")
# print(elms_news)
for elem in elms_news:
    print(elem.a.string)
    print(elem.a["href"], end="\n\n")