import requests

URL = "https://www.yahoo.co.jp"
response = requests.get(URL)
print(response.text)
print(response.status_code)