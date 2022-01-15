import requests

URL = "https://www.yahoo.co.jp"
response = requests.get(URL)
print(response.text)
print(response.status_code)

print(response.content)
print(response.encoding)

for key, value in response.headers.items():
    print(key, "  ", value)