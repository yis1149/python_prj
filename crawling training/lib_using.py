import requests
from bs4 import BeautifulSoup

response = requests.get("https://xn--sh1bx7bj4cm6h09ezw0a.com/")
html = response.text

soup = BeautifulSoup(html, "html.parser")

items = soup.select_one(".depth0 gnb_menu0")





print(items)
