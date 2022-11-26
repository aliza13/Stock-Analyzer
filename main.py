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
print(tickers)

# def startDate():
#     start = input("Start date? YYYY-MM-DD format: ")
#     return start 
# 
# def endDate():
#     end = input("End date? YYYY-MM-DD format: ")
#     return end 
# 
# startAt = startDate()
# endAt = endDate()
# need to iterate through tickers though
# df = yf.Ticker(tickers)


def GetstockInfo():
    """Returns stock info"""
    infoAbt = []
    for i in tickers:
        # one
        infoAbt.append(yf.Ticker(i).info['symbol']) 
        infoAbt.append(yf.Ticker(i).info['marketCap']) 
        # infoAbt.append(yf.Ticker(i).info)
    return infoAbt #returns long list of all Stock info 
    # .history(period="1mo") etc 1d, 5d, 2y, ytd, max
    # data = yf.download("SPY AAPL MSFT", start="2019-08-30", end="2020-01-31")

allTheInfo = GetstockInfo()

stuffToSee = ['dividendYield', 'marketCap', 'previousClose', 'regularMarketOpen', 'fiftyTwoWeekHigh']

mydf = pd.DataFrame(allTheInfo)
# ticker as index rather than a #
# mydf = mydf.set_index('symbol')
mydf[mydf.columns[mydf.columns.isin(stuffToSee)]]

print(mydf)


""" I want to select out the following info... 'symbol' 'dividendYield' 'marketCap' 'previousClose' 'regularMarketOpen' 'fiftyTwoWeekHigh' (Low) """

#     # can do .info["dayHigh"] or "fiftyTwoWeekLow" etc
# mydf = pd.DataFrame(data= infoOfStock, columns= ['Stock', 'currentPrice'])
# print(mydf)


""" 
# tickername.dividends
# use period 1m or 30m etc
# start/end parameters "
# 

"""