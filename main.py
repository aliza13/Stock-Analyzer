# Stock Analyzer Project 

import pandas as pd 
import yfinance as yf 
import datetime 


 # input and output

def getTick():
    "This function asks the user for input and returns what ticker they are requesting"
    userTicker = input("Type ticker of stock information to see: ")
    while userTicker != str:
            print("That is not a real ticker")
            userTicker = input("Type ticker of stock information to see: ")
            break

    return userTicker


whateverTick = getTick()


#tickerdata = yf.Ticker(whateverTick)
#tickerinfo = tickerdata.info
#print(tickerinfo)

""" 
def get_ticker()
    userinput = input("What ticker symbol").uppercase
    datetime 
    yfCall = yf.Ticker(userinput)
    tickerInfo = yfCall.info
# tickername.dividends
# use period 1m or 30m etc
# start/end parameters "
# 

"""