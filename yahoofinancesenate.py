import yfinance as yf
import datetime
import pandas as pd

'''def getPersonTickers(lastName, firstName):
    # call to database on senator's first / last name, return tickers associated with that senator
    tickersList = []
'''
holdingDict = { 'StockName' : ['TestTicker'], 'PriceJan20' : ['1'],'PriceMid20' : ['2'], 'PriceEnd20': ['3']}


def searchTicker(tickersymbol):
    tickerdata = yf.Ticker(tickersymbol)
    tickerinfo = tickerdata.info
    #print(tickerinfo)
    investment = tickerinfo['shortName']
    #sector = tickerinfo['sector']
    #industry = tickerinfo['industry']
    print(investment) #, sector, industry)

    #today = datetime.datetime.today().isoformat()
    #print('Today is: ' + today)
    #tickerDF = tickerdata.history(period='1d',start='2019-12-31', end='2021-1-1')
    tickerDFStart=tickerdata.history(period='1d',start='2019-12-30',end='2020-1-1')
    tickerDFMid=tickerdata.history(period='1d',start='2020-5-30',end='2020-7-1')
    tickerDFEnd=tickerdata.history(period='1d',start='2020-12-30',end='2021-1-1')
    #priceStart=tickerDF['Close'].iloc[0]
    #priceMid =tickerDF['Close'].iloc[147]
    #priceEnd=tickerDF['Close'].iloc[-1]
    priceStart2=tickerDFStart['Close'].iloc[1]
    priceMid2=tickerDFMid['Close'].iloc[1]
    priceEnd2=tickerDFEnd['Close'].iloc[1]
    #iloc numbers
    # 125 = 6.31.20 ; 147 = 7.31.20
    #
    #priceTarget=tickerDF['Close'].iloc['2020-7-31']
    #absChange=priceEnd-priceStart
    #yearlyReturn= absChange / priceStart * 100
    '''print(investment +' price start = ' + str(priceStart2)) #+ ' ' + str(priceStart2))# , yearlyReturn)
    print(investment +' price mid = ' + str(priceMid)+ ' ' + str(priceMid2))
    print(investment +' price end = ' + str(priceEnd2)) #' ' +  str(priceEnd2))
    ''''''
    a = investment +' price start , ' + str(priceStart2) #+ ' ' + str(priceStart2))# , yearlyReturn)
    b = investment +' price mid , ' + str(priceMid2) #+ ' ' + str(priceMid2)
    c = investment +' price end , ' + str(priceEnd2) #' ' +  str(priceEnd2))
    '''
    #print('Dollar Price Change = ' + str(absChange) + '. \nPercentage Price Change = ' + str(percentageChange) + '%.')

    #print(tickerDF)
    #tickerDF.to_csv('babby.csv')
    #create list of the statements
    a = tickersymbol
    b = priceStart2
    c = priceMid2
    d = priceEnd2
    data = [a, b, c, d]
    # turn it into a df
    holdingDict['StockName'].append(a)
    holdingDict['PriceJan20'].append(b)
    holdingDict['PriceMid20'].append(c)
    holdingDict['PriceEnd20'].append(d)
    #print('Dollar Price Change = ' + str(absChange) + '. \nPercentage Price Change = ' + str(percentageChange) + '%.')
    #print(tickerDF)
    #data.to_csv('the_best_data_frame_ever.csv')
    # python


tickerstosearch=['VFIAX','VEUSX', 'VIAAX', 'VEMAX', 'FEZ', 'PSX', 'SIRI']
for ticker in range (0, len(tickerstosearch)):
    searchTicker(tickerstosearch[ticker])
#searchTicker(tickerstosearch) #Intercontinental Exchange ticker
#data = pd.DataFrame(data)
tickerHolder = pd.DataFrame(holdingDict)
print(pd.DataFrame.head(tickerHolder))
tickerHolder.to_csv('HagertyPriceData6.csv')
