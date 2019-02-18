from abc import ABCMeta, abstractmethod
from LBCProperties.LBCHeader import LBCHeader
from functools import reduce 
import operator
import requests
import json

class LBCScrapper(metaclass=ABCMeta):
    def __init__(self, location):
        super().__init__()
        self.url        = "https://www.leboncoin.fr/"
        self.location   = location
        self.articles   = []
        self.last_pid   = 0
        self.session    = requests.Session()
        self.session.headers.update(LBCHeader.HEADER.value)

    def _merge_lists(self, iterable):
        return reduce(operator.concat, iterable)

    def store_to_json(self, filename="data.json"):
        """
            Store to json articles previously scrapped with following formation : 
            {
                "last-pid" : 0,
                "ID" : {
                    "title"     : XXX,
                    "price"     : XXX,
                    "location"  : XXX,
                    "link"      : XXX
                }
            }
            :param  filename:   the file name where to store data
            :type   filename:   str
            :returns:           none
            :rtype:             none
        """
        to_json = {"last-pip" : self.last_pid}
        if len(self.articles) > 0:
            with open(filename, "w", encoding="utf-8") as outfile:
                for i, item in enumerate(self.articles):
                    to_json[i] = item.format_to_json()
                outfile.write(json.dumps(to_json, ensure_ascii=False, indent=6))

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