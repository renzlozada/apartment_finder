import os
from bs4 import BeautifulSoup
import requests

apartments_url = os.environ["apartments_url"]
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0",
    "Accept-Encoding": "gzip, deflate",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "DNT": "1",
    "Connection": "close",
    "Upgrade-Insecure-Requests": "1"
}


class HouseDataBot:
    def __init__(self):
        self.addresses = []
        self.prices = []
        self.links = []

    def get_data(self):
        apartments_response = requests.get(url=apartments_url, headers=headers)
        apartments_site = apartments_response.text
        soup = BeautifulSoup(apartments_site, "html.parser")
        property_pricing = soup.find_all(class_="property-pricing")
        property_address = soup.find_all(class_="property-address")
        property_link = soup.find_all(class_="property-link")

        for price in property_pricing:
            self.prices.append(price.text)
        for address in property_address:
            self.addresses.append(address.text)
        # This checks for duplicates since the links being provided are sometimes a duplicate
        # of 2 or 3.
        for link in property_link:
            url_link = link.get("href")
            if url_link not in self.links:
                self.links.append(url_link)
            else:
                pass
