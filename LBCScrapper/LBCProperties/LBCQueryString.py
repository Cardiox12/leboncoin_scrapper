from abc                    import ABCMeta, abstractmethod
from .LBCQueryStringEnum    import LBCQueryStringEnum
import re

class LBCQueryString(metaclass=ABCMeta):
    def __init__(self, location):
        super().__init__(  )
        self.query_string   = LBCQueryStringEnum.LOCATION.value + location
        self.sort_string    = [item.value for item in LBCQueryStringEnum if item != LBCQueryStringEnum.NEW_PAGE.value]

    @abstractmethod
    def append(self, url):
        pass

    def _sanitize(self):
        for query in self.sort_string:
            self.query_string = self.query_string.replace(query, "")

    def older(self):
        self._sanitize()
        return LBCQueryStringEnum.OLDER.value

    def price_increase(self):
        self._sanitize()
        return LBCQueryStringEnum.INCREASE.value

    def price_decrease(self):
        self._sanitize()
        return LBCQueryStringEnum.DECREASE.value

    def increment(self, url, i):
        self.query_string = re.sub(r'(&page=\d*)', '', self.query_string)
        self.query_string += f"{LBCQueryStringEnum.NEW_PAGE.value}{i}"
        return url + self.query_string