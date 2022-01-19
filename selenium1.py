from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
import csv
import datetime

URL = "https://www.google.com"
Search_words = "python"
csv_date = datetime.datetime.today().strftime("%Y%m%d")
print(csv_date)

options = Options()
options.add_argument('--headless')
driver = webdriver.Chrome("./chromedriver", options=options)

driver.get(URL)

search_bar = driver.find_element_by_name("q")
search_bar.send_keys(Search_words)
search_bar.submit()

# count = 0
# while True:
#     count = count + 1
#     sleep(1)
#     for element_h3 in  driver.find_elements_by_xpath("//a/h3"):
#         print(element_h3.text)
#         element_a = element_h3.find_element_by_xpath("..")
#         print(element_a.get_attribute("href"))

#     next_link = driver.find_element_by_id("pnnext")
#     # print(next_link)
#     driver.get(next_link.get_attribute("href"))

#     if count > 4:
#         break

