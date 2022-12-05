# Stock Analyzer Project 

from multiprocessing.sharedctypes import Value
import pandas as pd 
import yfinance as yf 

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


def startDate():
    startingAt = input("Start date? YYYY-MM-DD format: ")
    return startingAt 

def endDate():
    endingAt = input("End date? YYYY-MM-DD format: ")
    return endingAt 

dfCol = ['Symbol','Dividend Yield', 'Market Cap', 'Previous Close', 'Regular Market Open', '52 Week High']

def GrabWantedData(tickerList):
    stuffToSee = ['symbol','dividendYield', 'marketCap', 'previousClose', 'regularMarketOpen', 'fiftyTwoWeekHigh']
    finalList = []
    for i in tickerList:
        infoAbt = yf.Ticker(i).info
        prettierList = [] 
        for item in stuffToSee:
            prettierList.append(infoAbt[item])
        finalList.append(prettierList)
    mydf = pd.DataFrame(finalList, columns=dfCol)
    mydf = mydf.set_index('Symbol')
    print(mydf)
    # makes a comma seperated Values file!
    # mydf.to_csv(r'csvFileOfStockInfo.csv')


#GrabWantedData(tickers)

beginDate = startDate()
endDateInfo = endDate()

# tickerList parameter is tickers list that user inputs
def showingHistory(tickerList):
    historyList = []
    for i in tickerList: # i is ea ticker symbol in list ex. AAPL. PFE
        historyCall = yf.Ticker(i).history(start=beginDate, end=endDateInfo)
        historyList.append(historyCall)
        # the history call is what the df should be
    for j in historyList: # takes list and splits it into two DFs
        dfItem = pd.DataFrame(j)
        print(dfItem)


showingHistory(tickers)

""" csv file --> excel
bring into a df or csv to compare them 1:1
func
call s/e date
"""

# final list has multiple lists from prettierList 
# finalList[[prettierList['symbol': 'AAPL']]] data structure 