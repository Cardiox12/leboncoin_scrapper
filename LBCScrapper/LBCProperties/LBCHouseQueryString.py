from LBCQueryString import LBCQueryString

class LBCHouseQueryString(LBCQueryString):
    def __init__(self, query_string=""):
        super().__init__(query_string)
        self.query_string = query_string