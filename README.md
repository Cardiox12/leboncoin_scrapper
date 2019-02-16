# house-scrapper

A house scrapper automation for [Le Bon Coin](https://www.leboncoin.fr/).

__Goals__ :
The main goal of this project is to scrap and filter house announce on [Le Bon Coin](https://www.leboncoin.fr/) and will release\
a resume of new announces with [Twilio](https://www.twilio.com/) at certain interval determined by the user.

__Steps__ :
This is a resume of script steps. 

1. _Request each pages_ 
2. _Parse each pages_ : 
    - title
    - price
    - location
    - link
3. _Store data in JSON_ 
4. _Make the difference between JSON and actual DATA (implement dynamic search, scrap only end page)_
    - if difference then
        - send resume of new announces with twilio