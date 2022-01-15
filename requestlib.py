import requests

URL = "https://www.yahoo.co.jp"
response = requests.get(URL)
print(response.text)
print(response.status_code)

print(response.content)
print(response.encoding)

for key, value in response.headers.items():
    print(key, "  ", value)

user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36"
header = {"user_agent": user_agent}

response = requests.get(URL, headers= header)
print(response.status_code)