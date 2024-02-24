import requests
import lxml
from bs4 import BeautifulSoup
url = "https://cash-backer.club/shops"
while True:
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        all_products_rate = soup.find_all("div", class_="shop-rate")
        for rate in all_products_rate:
            print("Rate:", rate.text.strip(">>>"))
        all_products_title = soup.find_all("div", class_="shop-title")
        for title in all_products_title:
            print("Tile:", title.text.strip("<<<"))
        pagination = soup.find('a', href=True)
        if not pagination:
            break