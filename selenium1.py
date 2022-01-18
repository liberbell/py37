from selenium import webdriver
from time import sleep

URL = "https://www.google.com"
driver = webdriver.Chrome("./chromedriver")
driver.get(URL)