from    LBCProperties.LBCDomTarget          import LBCDomTarget
from    LBCProperties.LBCArticle            import LBCArticle
from    LBCProperties.LBCQueryString        import LBCQueryString
from    LBCProperties.LBCQueryStringEnum    import LBCQueryStringEnum
from    LBCProperties.LBCQueryStringEnum    import LBCQueryStringCitiesEnum
from    LBCProperties.LBCPrice              import LBCPrice     as Price
from    LBCProperties.LBCSquare             import LBCSquare    as Square
from    LBCProperties.LBCRooms              import LBCRooms     as Rooms
from    LBCProperties.LBCHouseProperties    import LBCHouseProperties
from    LBCScrapper                         import LBCScrapper
from    bs4                                 import BeautifulSoup 
import  json 

class LBCHouseScrapper(LBCScrapper):
    """
        LBCHouseScrapper is an object for scrappping Le Bon Coin real estate.
        :param  location: The location to search
        :type   location: LBCQueryStringCitiesEnum
        :param  house_properties: The house properties
        :type   house_properties: LBCHouseProperties
        :param  query_string: The query string for url
        :type   query_string: LBCQueryString
    """
    def __init__(self, location, house_properties, query_string):
        super().__init__(location)
        self.location           = location
        self.house_properties   = house_properties
        self.query_string       = query_string

    def store_to_json(self, filename="data.json"):
        pass

    def get_from_json(self, filename="data.json"):
        with open(filename, "r") as f:
            return json.load(f)

    def parse_articles(self):
        pass

    def get_articles(self):
        query_string = LBCQueryString()

    def get_titles(self):
        pass

    def get_prices(self):
        pass

    def get_locations(self):
        pass
    
    def get_links():
        pass