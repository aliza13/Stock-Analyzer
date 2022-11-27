# Stock Analyzer Project 

from multiprocessing.sharedctypes import Value
import pandas as pd 
import yfinance as yf 
import datetime 

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
      
getTick()        

def GetstockInfo():
    """Returns stock info"""
    infoAbt = []
    for i in tickers:
        infoAbt.append(yf.Ticker(i).info)
    return infoAbt #returns long list of all Stock info 
    # .history(period="1mo") etc 1d, 5d, 2y, ytd, max
    # data = yf.download("SPY AAPL MSFT", start="2019-08-30", end="2020-01-31")
allTheInfo = GetstockInfo()

def GrabWantedData():
    # key list
    stuffToSee = ['symbol','dividendYield', 'marketCap', 'previousClose', 'regularMarketOpen', 'fiftyTwoWeekHigh']
    prettierList = [] # will store values of ^^ 
    item1 = allTheInfo[0] # need to iterate through all the desired tickers
    for i in stuffToSee:
        prettierList.append(item1[i])
    print(prettierList)
    return prettierList

for key, item in allTheInfo[0].items():
    print(key, item)

#or for item in allTheInfo[0].items():
#will print out a bunch of list


# mydf = pd.DataFrame(allTheData)
# ticker as index rather than a #
# mydf = mydf.set_index('symbol') # does not work
#     # can do .info["dayHigh"] or "fiftyTwoWeekLow" etc
# mydf = pd.DataFrame(data= allTheData, columns= ['Stock', 'currentPrice'])
# print(mydf)
