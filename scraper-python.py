# scraper-python.py
# To run this script, paste `python scraper-python.py` in the terminal

import requests
from bs4 import BeautifulSoup


def scrape():
    url = 'https://www.finsmes.com/2024/12/happyrobot-raises-15-6m-in-series-a-funding.html'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    print(soup)


if __name__ == '__main__':
    scrape()