import json
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep

URL = "https://www.instagram.com/"

with open("insta_secret.json") as f:
    insta_key = json.load(f)
ID = insta_key["id"]
PASSWORD = insta_key["password"]

# print(ID, PASSWORD)
options = Options()
options.add_argument('--headless')
# driver = webdriver.Chrome("./chromedriver", options=options)
driver = webdriver.Chrome("./chromedriver")
driver.get(URL)

sleep(2)

error_flag = False


# <input aria-label="Phone number, username, or email" aria-required="true" autocapitalize="off" autocorrect="off" maxlength="75" name="username" type="text" class="_2hvTZ pexuQ zyHYP" value="">
try:
    print()
    username_input = driver.find_element_by_xpath("//input[@aria-label='Phone number, username, or email']")
except Exception:
    error_flag = True
    print("Error when input ID or Password.")