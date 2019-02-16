from abc import ABC
from LBCQueryStringEnum import LBCQueryStringEnum

class LBCQueryString(ABC):
    def __init__(self, query_string=""):
        self.query_string   = query_string
        self.sort_string    = [item.value for item in LBCQueryStringEnum]
    
    def _sanitize(self):
        for query in self.sort_string:
            self.query_string = self.query_string.replace(query, "")

    def older(self):
        self._sanitize()
        self.query_string += LBCQueryStringEnum.OLDER.value
        return self.query_string

    def price_increase(self):
        self._sanitize()
        self.query_string += LBCQueryStringEnum.INCREASE.value
        return self.query_string

    def price_decrease(self):
        self._sanitize()
        self.query_string += LBCQueryStringEnum.DECREASE.value
        return self.query_string