# Stock Analyzer Project 

from multiprocessing.sharedctypes import Value
import pandas as pd 
import yfinance as yf 
import datetime 

#aTick = yf.Ticker('APPL').info
#print(aTick)

tickers = []

def getTick():
    "This function asks the user for input and returns what ticker(s) they requested"
    while True:
        try:
            howMany = int(input("How many stocks do you want to compare?: "))
            if howMany > 4 or howMany < 1:
                raise ValueError
            break    
        except ValueError:
            print("That is not a valid number")        

    while howMany <= howMany:
        try:
            userTicker = input("Type ticker of stock information to see: ")
            if len(userTicker) > 5:
                raise ValueError
            tickers.append(str(userTicker))
            if len(tickers) > howMany -1: 
                break
        except ValueError:
            print("That is not a valid ticker")        

# file that has all ticker names... if input != a name in the list then        
getTick()        

def GetstockInfo():
    """Returns stock info"""
    infoAbt = []
    for i in tickers:
        # infoAbt.append(yf.Ticker(i).info['symbol']) 
        # infoAbt.append(yf.Ticker(i).info['marketCap']) 
        infoAbt.append(yf.Ticker(i).info)
    return infoAbt #returns long list of all Stock info 
    # .history(period="1mo") etc 1d, 5d, 2y, ytd, max
    # data = yf.download("SPY AAPL MSFT", start="2019-08-30", end="2020-01-31")
allTheInfo = GetstockInfo()

def GrabWantedData():
    # key list
    stuffToSee = ['dividendYield', 'marketCap', 'previousClose', 'regularMarketOpen', 'fiftyTwoWeekHigh']
    prettierList = [] # will store values of ^^ 
    item1 = allTheInfo[0]
    for i in stuffToSee:
        prettierList.append(item1[i])
    print(prettierList)

stuff = GrabWantedData()
print(stuff)

# mydf = pd.DataFrame(allTheInfo)
# ticker as index rather than a #
# mydf = mydf.set_index('symbol')
# mydf[mydf.columns[mydf.columns.isin(stuffToSee)]]

#     # can do .info["dayHigh"] or "fiftyTwoWeekLow" etc
# mydf = pd.DataFrame(data= infoOfStock, columns= ['Stock', 'currentPrice'])
# print(mydf)
