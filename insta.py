import json
from selenium import webdriver
from time import sleep

with open("insta_secret.json") as f:
    insta_key = json.load(f)
ID = insta_key["id"]
PASSWORD = insta_key["password"]

# print(ID, PASSWORD)