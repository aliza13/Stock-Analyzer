import pandas as pd 

dataList = ["Hello", "World", "!"]

mydf = pd.DataFrame(dataList)

mySeries = pd.Series(dataList)

print(dataList[1])
# return value at index, can do multiple
print(mySeries)
# data type = object
print(mydf)
# print(pd.__version__)

a = ["A", "B", "C"]
# newIndexABC = (a, pd.index == ["z", "y", "x"])
# pd has no value of index
# zyx, aka labels

# daysOfWeek = {"day1": "Monday", "day2": "Tuesday", "day3": "Wednesday"}
# dowSeries = pd.Series(daysOfWeek)
# print(dowSeries)

dowSet = {
    "numOfDay": [1, 2, 3, 4, 5, 6, 7],
    "day": ["Mon", "Tu", "Wed", "Th", "Fri", "Sat", "Sun"],
    "fav": ["False", "False", "True", "False", "False", "False", "False"]
} # must have same # of values
dowdf2 = pd.DataFrame(dowSet)
print(dowdf2)
# .info() shows non-null, int64, object etc for columns

print(dowdf2.loc[2])
# grabs second index from all data set
# (dowdf2.loc[[2,4]]) only these two
# (dowdf2.loc[2:4]) all 2-4

# thisFile = pd.read_csv('NameOfCSV.csv')
# print entire df (thisFile.to_string())

print(dowdf2.head(4)) # or .tail

"""
JSON keys from Yahoo Finance API
ex. ['symbol', 'longName', 'sector' 'industry','city', 'state', 'regularMarketPreviousClose']


def getCompanyInfo(tickers, df_cols, api_cols):
    complete_list = [] #List to hold the lists generated for each row of values that we will use in company_df

    #Loops through each ticker, gets all the information, and pulls the values from the desired feilds in api_col_list
    for symbol in tickers:
        ticker = yf.Ticker(symbol)
        company_info = ticker.info
        val_list = []

    #Appends values for each api_column in api_column_list for a ticker and appends them to a list for that ticker
        for api_column in api_cols:
            val_list.append(company_info[api_column])

    #Appends the list of values for a ticker to the complete_list
        complete_list.append(val_list)

    #Generate and print dataframe with lists of ticker values
    company_df = pd.DataFrame(complete_list, columns=df_cols)
    print(company_df)
    pd.company_df.to_csv()

getCompanyInfo(tickers_list, df_col_list, api_col_list)


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

tickers_list = ['MRNA', 'XPO', 'ICE', 'GILD']
#Column names for dataframe *must parallel the api_col_list
df_col_list = ['Ticker', 'Company Name', 'Sector']
#List of JSON keys from Yahoo Finance API
api_col_list = ['symbol', 'longName', 'sector']

def getCompanyInfo(tickers, df_cols, api_cols):
    complete_list = [] #List to hold the lists generated for each row of values that we will use in company_df

    #Loops through each ticker, gets all the information, and pulls the values from the desired feilds in api_col_list
    for symbol in tickers:
        ticker = yf.Ticker(symbol)
        company_info = ticker.info
        val_list = []

    #Appends values for each api_column in api_column_list for a ticker and appends them to a list for that ticker
        for api_column in api_cols:
            val_list.append(company_info[api_column])

    #Appends the list of values for a ticker to the complete_list
        complete_list.append(val_list)

    #Generate and print dataframe with lists of ticker values
    company_df = pd.DataFrame(complete_list, columns=df_cols)
    print(company_df)
    pd.company_df.to_csv()


getCompanyInfo(tickers_list, df_col_list, api_col_list)



"""
