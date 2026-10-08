import requests
from bs4 import BeautifulSoup





url = "https://books.toscrape.com/"

response = requests.get(url)

soup = beautifulsoup
print("status", response.status_code)
print(response.text[:500])