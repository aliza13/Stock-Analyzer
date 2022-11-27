# Stock Analyzer Project 

from multiprocessing.sharedctypes import Value
import pandas as pd 
import yfinance as yf 
import tkinter as tk
from tkinter import *

root = tk.Tk()

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

    # .history(period="1mo") etc 1d, 5d, 2y, ytd, max
    # data = yf.download("SPY AAPL MSFT", start="2019-08-30", end="2020-01-31")
# allTheInfo = GetstockInfo()


def GrabWantedData(tickerList):
    stuffToSee = ['symbol','dividendYield', 'marketCap', 'previousClose', 'regularMarketOpen', 'fiftyTwoWeekHigh']
    finalList = []
    for i in tickerList:
        infoAbt = yf.Ticker(i).info
        prettierList = [] 
        for item in stuffToSee:
            prettierList.append(infoAbt[item])
        finalList.append(prettierList)
    mydf = pd.DataFrame(finalList, columns=stuffToSee)
    mydf = mydf.set_index('symbol')
    frame = Canvas(root)
    frame.pack(mydf)

GrabWantedData(tickers)

# final list has multiple lists from prettierList 
# finalList[[prettierList['symbol': 'AAPL']]]

root.mainloop()

# mydf = mydf.set_index('symbol') # does not work
#     # can do .info["dayHigh"] or "fiftyTwoWeekLow" etc
