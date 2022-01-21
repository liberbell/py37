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
# <input aria-label="電話番号、ユーザーネーム、メールアドレス" aria-required="true" autocapitalize="off" autocorrect="off" maxlength="75" name="username" type="text" class="_2hvTZ pexuQ zyHYP" value="">
# <input aria-label="Password" aria-required="true" autocapitalize="off" autocorrect="off" name="password" type="password" class="_2hvTZ pexuQ zyHYP" value="">
try:
    print()
    username_input = driver.find_element_by_xpath("//input[@aria-label='電話番号、ユーザーネーム、メールアドレス']")
    username_input.send_keys(ID)
    sleep(1)

    password_input = driver.find_element_by_xpath("//input[@aria-label='パスワード']")
    password_input.send_keys(PASSWORD)
    sleep(1)

    login_button = driver.find_element_by_xpath("//button[@type='submit']")
    login_button.submit()
    sleep(1)

    # <button class="aOOlW   HoLwm " tabindex="0">後で</button>

except Exception:
    error_flag = True
    print("Error when input ID or Password.")

if error_flag is False:
    try:
        sleep(1)
        saveenv_button = driver.find_element_by_xpath("//button[text()='後で']")
        saveenv_button.click()
        sleep(1)
        notnow_button = driver.find_element_by_xpath("//button[text()='後で']")
        notnow_button.click()
        sleep(1)

    except Exception:
        pass

target_username = "onerepublic"
if error_flag is False:
    try:
        target_profiel_url = URL + target_username
        driver.get(target_profiel_url)
        sleep(2)

    except Exception:
        print("Error when search keyword.")
        error_flag = True

if error_flag is False:
    try:
        post_count = driver.find_element_by_xpath("//span[text()='投稿']").text
        post_count = post_count.replace("投稿", "")
        post_count = post_count.replace("件", "")
        print(post_count)
        sleep(2)

    except Exception:
        print("Can't get post counts.")
        error_flag = True