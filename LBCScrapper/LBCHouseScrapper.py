from    pprint                              import pprint 
from    LBCProperties.LBCDomTarget          import LBCDomTarget
from    LBCProperties.LBCArticle            import LBCArticle
from    LBCProperties.LBCQueryStringEnum    import LBCQueryStringEnum
from    LBCProperties.LBCQueryStringEnum    import LBCQueryStringCitiesEnum
from    LBCProperties.LBCHouseQueryString   import LBCHouseQueryString
from    LBCProperties.LBCPrice              import LBCPrice     as Price
from    LBCProperties.LBCSquare             import LBCSquare    as Square
from    LBCProperties.LBCRooms              import LBCRooms     as Rooms
from    LBCProperties.LBCHouseProperties    import LBCHouseProperties
from    LBCScrapper                         import LBCScrapper
from    bs4                                 import BeautifulSoup 
import  json 
import  re

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
    def __init__(self, location, house_properties):
        super().__init__(location)
        self.location           = location
        self.house_properties   = house_properties
        self.query_string       = LBCHouseQueryString(self.location)

    def parse_articles(self):
        pass

    def get_articles(self):
        """
            Get articles method scrap all pages of Le Bon Coin articles
            :returns:   A list of LBCArticle objects
            :rtype:     list
        """
        increment   = 0
        titles      = []
        prices      = []
        locations   = []
        links       = []

        while True:
            url         = self.query_string.increment(self.url, increment)

            request     = self.session.get(url)
            scrapper    = BeautifulSoup(request.text, "html.parser")

            articles = scrapper.find_all("li", class_=LBCDomTarget.ARTICLE.value)
            if len(articles) == 0:
                break
            increment += 1

            print(url)

            titles.append(self.get_titles(articles))
            prices.append(self.get_prices(articles))
            locations.append(self.get_locations(articles))
            links.append(self.get_links(articles))
        
        self.last_pid = increment
        for title, price, location, link in zip(self._merge_lists(titles), self._merge_lists(prices), 
                                                self._merge_lists(locations), self._merge_lists(links)):
            self.articles.append(
                LBCArticle(title, price, location, link)
            )
        
        return self.articles
        
    def get_titles(self, articles):
        titles = []
        for article in articles:
            titles.append(
                article.find("span", {"data-qa-id": "aditem_title"}).text
            )
        return titles

    def get_prices(self, articles):
        prices = []
        for article in articles:
            prices.append(
                re.search(r'^\d*', article.find("span", class_=LBCDomTarget.PRICE.value).text).group(0)
            )
        
        return prices

    def get_locations(self, articles):
        locations = []
        for article in articles:
            locations.append(
                article.find("p", LBCDomTarget.LOCATION.value).text
            )

        return locations

    def get_links(self, articles):
        links = []
        for article in articles:
            links.append(
                self.url[:-1] + article.find("a").attrs.get('href')
            )
        return links


if __name__ == '__main__':
    location = LBCQueryStringCitiesEnum.AVIGNON.value
    house_properties = LBCHouseProperties(Price(0, 100), Rooms(0, 100), Square(0, 100))

    lbs = LBCHouseScrapper(location, house_properties)
    lbs.get_articles()
    lbs.store_to_json()