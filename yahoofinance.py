import yfinance as yf
import datetime
import pandas as pd

def getPersonTickers(lastName, firstName):
    # call to database on senator's first / last name, return tickers associated with that senator
    tickersList = []


def searchTicker(tickersymbol):
    tickerdata = yf.Ticker(tickersymbol)
    tickerinfo = tickerdata.info
    #print(tickerinfo)
    investment = tickerinfo['shortName']
    sector = tickerinfo['sector']
    industry = tickerinfo['industry']
    print(investment, sector, industry)

    today = datetime.datetime.today().isoformat()
    print('Today is' + today)
    tickerDF = tickerdata.history(period='1d',start='2020-1-1', end='2021-1-1')
    priceLast=tickerDF['Close'].iloc[-1]
    priceYest=tickerDF['Close'].iloc[-2]
    absChange=priceLast-priceYest
    percentageChange= absChange / priceYest * 100
    print(investment +' price last = ' + str(priceLast))
    print(investment +' price yesterday = ' + str(priceYest))
    print('Dollar Price Change = ' + str(absChange) + '. \nPercentage Price Change = ' + str(percentageChange) + '%.')
    print(tickerDF)
    tickerDF.to_csv('babby.csv')


searchTicker('ICE') #Intercontinental Exchange ticker
