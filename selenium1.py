from tokenize import Ignore
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
import csv
import datetime

URL = "https://www.google.com"
Search_words = "python"
csv_date = datetime.datetime.today().strftime("%Y%m%d")
# print(csv_date)
csv_file_name = "google_python_" + csv_date + ".csv"
file = open(csv_file_name, "w", encoding="cp932", errors="ignore")
writer = csv.writer(file, lineterminator="\n")
csv_header = ["No", "Title", "URL"]
writer.writerow(csv_header)

options = Options()
options.add_argument('--headless')
driver = webdriver.Chrome("./chromedriver", options=options)

driver.get(URL)

search_bar = driver.find_element_by_name("q")
search_bar.send_keys(Search_words)
search_bar.submit()

count = 0
rank = 1
while True:
    count = count + 1
    sleep(1)
    for element_h3 in  driver.find_elements_by_xpath("//a/h3"):
        csv_list = []
        csv_list.append(str(rank))
        # print(element_h3.text)
        csv_list.append(element_h3.text)
        element_a = element_h3.find_element_by_xpath("..")
        # print(element_a.get_attribute("href"))
        csv_list.append(element_a.get_attribute("href"))
        writer.writerow(csv_list)

    next_link = driver.find_element_by_id("pnnext")
    # print(next_link)
    driver.get(next_link.get_attribute("href"))
    rank = rank + 1

    if count > 4:
        break
file.close()