from abc import ABC, abstractmethod
from LBCProperties.LBCHeader import LBCHeader
import requests
import json

class LBCScrapper(ABC):
    def __init__(self, location: LBCQueryStringCitiesEnum):
        super().__init__()
        self.url        = "https://www.leboncoin.fr/"
        self.location   = self.location
        self.articles   = []
        self.last_pid   = 0
        self.session    = requests.Session()
        self.session.headers.update(LBCHeader.HEADER.value)

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