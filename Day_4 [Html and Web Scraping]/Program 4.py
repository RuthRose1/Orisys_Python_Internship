from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/") #link
print(response) #o/p -> response -> 200 ie,status success

print(response.text)