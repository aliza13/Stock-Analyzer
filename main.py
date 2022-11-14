# Stock Analyzer Project 

from tracemalloc import start
import pandas as pd 
import yfinance as yf 
import datetime 

#aTick = yf.Ticker('APPL').info
#print(aTick)

tickers = []

def getTick():
    "This function asks the user for input and returns what ticker they requested"
    howMany = int(input("How many stocks do you want to compare?: "))
    # how to make howMany only go up to 4
    while howMany <= howMany:
        # needs to be stricter on input
        userTicker = input("Type ticker of stock information to see: ")
        # file that has all ticker names... if input != a name in the list then
        # recalls userTicker
        tickers.append(str(userTicker))
        if len(tickers) > howMany -1:
            break
        
getTick()        
print(tickers)

def startDate():
    start = input("Start date? YYYY-MM-DD format: ")
    return start 

def endDate():
    end = input("End date? YYYY-MM-DD format: ")
    return end 

startAt = startDate()
endAt = endDate()
# need to iterate through tickers though
# df = yf.Ticker(tickers)

# def stockInfo():
#     # shows dividends 
#     whateverTick.dividends
#     # quarterly earnings
#     whateverTick.quarterly_earnings
#     # .history(period="1mo") etc 1d, 5d, 2y, ytd, max
#     # data = yf.download("SPY AAPL MSFT", start="2019-08-30", end="2020-01-31")
# 

# def yfCall():
#     """Returns stock info"""
#     tickerdata = yf.Ticker(whateverTick)
#     tickerinfo = tickerdata.info
#     # can do whateverTick.info["dayHigh"] or "fiftyTwoWeekLow" etc
#     #print(tickerinfo)
#     return tickerinfo 
# 
# infoOfStock = yfCall()
# mydf = pd.DataFrame(data= infoOfStock, columns= ['Stock', 'currentPrice'])
# print(mydf)


""" 
# tickername.dividends
# use period 1m or 30m etc
# start/end parameters "
# 

"""