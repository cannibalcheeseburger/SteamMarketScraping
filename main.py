from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup 
filename = "./csv/Steam.csv"
f = open(filename,"w")
headers = "Item_name, Price, Quantity, Game\n"
f.write(headers)
for i in range(1,3):
    url = 'https://steamcommunity.com/market/search?q=#p'+str(i)+'_popular_desc'
    print(url)
    uClient = uReq(url)
    page_html = uClient.read()
    uClient.close()
    page_soup = soup(page_html,"html.parser")
    containers = page_soup.findAll("div",{"class":"market_listing_row market_recent_listing_row market_listing_searchresult"})
    for container in containers: 
        quantity = container.span.span["data-qty"]
        item_container = container.findAll("span",{"class":"market_listing_item_name"})
        item_name = item_container[0].text 
        price_container = container.findAll("span",{"class":"sale_price"})
        price = price_container[0].text
        game_container = container.findAll("span",{"class":"market_listing_game_name"})
        game = game_container[0].text
        print(item_name+"\t"+price+"\t"+quantity+"\t"+game)
        f.write(item_name + "," + price + "," + quantity + "," + game +"\n")
f.close()    






















