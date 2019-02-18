from .LBCQueryString        import LBCQueryString
from .LBCQueryStringEnum    import LBCQueryStringEnum

class LBCHouseQueryString(LBCQueryString):
    def __init__(self, location):
        super().__init__(location)
        self.query_base     = "recherche/?category=10"
        self.query_type     = LBCQueryStringEnum.REAL_ESTATE.value
        self.query_base     += self.query_string + self.query_type
        self.query_string   = self.query_base

    def append(self, url):
        return url + self.query_string