from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup 
import os
from texttable import Texttable
while True:
    t = Texttable()
    url = 'https://steamcommunity.com/market/'
    uClient = uReq(url)
    page_html = uClient.read()
    uClient.close()
    page_soup = soup(page_html,"html.parser")
    containers = page_soup.findAll("div",{"class":"market_listing_row market_recent_listing_row market_listing_searchresult"})
    count = 0
    os.system('clear')
    prev_price = 0
    t.add_rows([["Sno","Name","Price","Quantity","Game"]])
    for container in containers: 
        count = count + 1
        quantity = container.span.span["data-qty"]
        item_container = container.findAll("span",{"class":"market_listing_item_name"})
        item_name = item_container[0].text 
        price_container = container.findAll("span",{"class":"sale_price"})
        price = price_container[0].text
        if prev_price > int(quantity):
            symbol = "!"
        elif prev_price < int(quantity):
            symbol = "|"
        elif prev_price == int(quantity) :
            symbol = "-"        
        game_container = container.findAll("span",{"class":"market_listing_game_name"})
        game = game_container[0].text
       # print(str(count)+"\t"+item_name+"\t"+price+"\t"+quantity+"\t"+game)
        t.add_rows([[count, item_name,price,quantity+symbol,game]])
        print(t.draw())
        prev_price = int(quantity)