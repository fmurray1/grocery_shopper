"""
This is a python tool to help with grocery shopping through amazon fresh/amazon prime now.
"""
from bs4 import BeautifulSoup
from typing import Optional
import requests

HEADERS = ({'User-Agent':
            'Mozilla/5.0 (X11 Linux x86_64)'
            'AppleWebKit/537.36 (KHTML, like Gecko)'
            'Chrome/44.0.2403.157 Safari/537.36',
            'Accept-Language': 'en-US, en;q=0.5'})


class Item():
    def __init__(self, name=None, url=None):
        self.url: Optional[str] = url
        self.name: Optional[str] = name


def get_grocery_item(item_to_buy: str):
    url = "something goest here"+item_to_buy

    webpage = requests.get(url, headers=HEADERS)
    search_results = BeautifulSoup(webpage.content)
    for potential_item in search_results.findall("i have no idea yet"):
        if get_correct_item(potential_item, item_to_buy):
            cart_item = Item(name=item_to_buy)
            break
    add_item_to_cart(cart_item)


# I think bs returns a string but im not 100%
def get_correct_item(potential_item: str, item: Item):
    pass


def add_item_to_cart(item):  # this is probably going to change
    pass
