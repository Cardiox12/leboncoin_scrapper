from abc import ABC, abstractmethod
from LBCHeader import LBCHeader
import requests
import json

class LBCScrapper(ABC):
    def __init__(self, url="https://www.leboncoin.fr/"):
        self.session = requests.Session()
        self.header = LBCHeader.HEADER
        self.articles = []
        self.last_pid = 0

    @abstractmethod
    def store_to_json(self, filename="data.json"):
        pass

    def get_from_json(self, filename="data.json"):
        with open(filename, "r") as f:
            return json.load(f)

    @abstractmethod
    def parse_articles(self):
        pass

    @abstractmethod
    def get_articles(self):
        pass

    @abstractmethod
    def get_titles(self):
        pass

    @abstractmethod
    def get_prices(self):
        pass

    @abstractmethod
    def get_locations(self):
        pass
    
    @abstractmethod
    def get_links():
        pass