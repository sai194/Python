import bs4
import requests
from bs4 import BeautifulSoup


def getStock(symbl):

    baseurl = 'https://finance.yahoo.com/quote/{symbl}?p={symbl}'
    url = baseurl.format(symbl = symbl)
    print(url)
    stockRequest = requests.get(url)
    soup = bs4.BeautifulSoup(stockRequest.text, features="html.parser")

    price = soup.find_all("div", {'class': 'My(6px) Pos(r) smartphone_Mt(6px)'})[0].find_all('span')[0].text
    daychange = soup.find_all("div", {'class': 'My(6px) Pos(r) smartphone_Mt(6px)'})[0].find_all('span')[1].text

    return {"symbl": symbl, "currentPrice": price, "day's-change": daychange}


userInput = input("Enter symbols as input arguments separated by spaces: ")
symbls = userInput.split(" ")
stocks = []
for symbl in symbls:
    stocks.append(getStock(symbl))

with open("stocks.txt", "w") as filehandle:
    for stock in stocks:
            filehandle.write(str(stock) +"\n")
print(*stocks, sep = "\n")
