#!/usr/bin/env python3.7
from bs4 import BeautifulSoup
from pprint import pprint 
from functools import reduce
import operator
import re
import requests
import json

class HouseInfo(object):
  def __init__(self, price=("min", "max"), rooms=("min", "max"), square=("min", "max")):
    self.price = price
    self.rooms = rooms
    self.square = square

class HouseScrapper(object):
  def __init__(self, url, infos=HouseInfo()):
    self.url = url
    self.infos = infos
    self.query_string = "recherche/?category=10"\
                        "&locations=Avignon_84000"\
                        "&real_estate_type=2,1"\
                        f"&price={infos.price[0]}-{infos.price[1]}"\
                        f"&rooms={infos.rooms[0]}-{infos.rooms[1]}"\
                        f"&square={infos.square[0]}-{infos.square[1]}"
    self.session = requests.Session()
    self.session.headers.update({
      'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.81 Safari/537.36',
      'Accept-Encoding': 'gzip, deflate, br',
      'Accept-Language': 'fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7'
    })
    self.articles = []
    self.infos = self.scrap_all()
    self.last_pid = 0
    self.penultimate_number_of_article = 0
  
  def scrap_all(self, start=1):
    page_id = start
    while True:
      request = self.session.get("".join([self.url, self.query_string, f"&page={page_id}"]))
      scrapper = BeautifulSoup(request.text, "html.parser")
      page_article = scrapper.find_all("li", class_="_3DFQ-")

      if len(page_article) == 0:
        break

      self.articles.append(page_article)
      print("".join([self.url, self.query_string, f"&page={page_id}"]))
      page_id += 1 
    
    self.last_pid = page_id - 1
    return self.articles

  def parse_all_infos(self):
    article_id = 1
    articles_info = {"titles": [], "prices": [], "locations": [], "links": []}

    for item in self.articles:
      for article in item:
          articles_info['titles'].append(
              [title.text for title in article.find_all("span", {"data-qa-id": "aditem_title"})]
            )
          
          articles_info['prices'].append(
              [re.search(r"\d{1,4}", price.text).group(0) for price in article.find_all("span", class_="_1NfL7")]
            )
          
          articles_info['locations'].append(
              [item.text for item in article.find_all("p", class_="_2qeuk")]
            )
          
          articles_info['links'].append(
              ["".join([self.url, item.attrs.get('href')[1:]]) for item in article.find_all("a")]
          )

    self.penultimate_number_of_article = len(articles_info['titles'])
    print(self.penultimate_number_of_article)
    articles_info['titles'] = self._merge_lists(articles_info['titles'])
    articles_info['prices'] = self._merge_lists(articles_info['prices'])
    articles_info['locations'] = self._merge_lists(articles_info['locations'])
    articles_info['links'] = self._merge_lists(articles_info['links'])
    return articles_info

  def store_info_to_json(self, filename="data.json"):
    parsed_info = {"last-pid" : self.last_pid}

    with open(filename, "w", encoding="utf-8") as outfile:
      for i, item in enumerate(zip(*self.infos.values())):
        parsed_info[i] = dict(
          (key, val) for key, val in zip([key.replace("s", "") for key in self.infos.keys()],
                                          item)
        )

      outfile.write(json.dumps(parsed_info, indent=4, ensure_ascii=False))

  def _merge_lists(self, iterable):
    return reduce(operator.concat, iterable)


base_url = "https://www.leboncoin.fr/" 
hs = HouseScrapper(base_url, HouseInfo(("min", "700")))
hs.parse_all_infos()