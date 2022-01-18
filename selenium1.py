from selenium import webdriver
from time import sleep

URL = "https://www.google.com"
Search_words = "python"
driver = webdriver.Chrome("./chromedriver")
driver.get(URL)

search_bar = driver.find_element_by_name("q")
search_bar.send_keys(Search_words)