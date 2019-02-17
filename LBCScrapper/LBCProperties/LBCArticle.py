class LBCArticle(object):
    """
        Article class representing a le bon coin article.
        
        :param  title:      the article title 
        :type   title:      str
        :param  price:      the article price 
        :type   price:      str
        :param  location:   the article location
        :type   location:   str
        :param  link:       the article title 
        :type   link:       str
    """
    def __init__(self, title, price, location, link):
        self.title = title
        self.price = price
        self.location = location
        self.link = link

    def format_to_json(self):
        """
            Transform LBCArticle into JSON format
            :return: a dictionnary representing the article
            :rtype: dict
        """
        return {
            "title"     : self.title,
            "price"     : self.price,
            "location"  : self.location,
            "link"      : self.link
        }