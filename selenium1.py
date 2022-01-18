from selenium import webdriver
from time import sleep

URL = "https://www.google.com"
Search_words = "python"
driver = webdriver.Chrome("./chromedriver")
driver.get(URL)

search_bar = driver.find_element_by_name("q")
search_bar.send_keys(Search_words)
search_bar.submit()

for element_h3 in  driver.find_elements_by_xpath("//a/h3"):
    print(element_h3.text)
    element_a = element_h3.find_element_by_xpath("..")
    print(element_a.text)