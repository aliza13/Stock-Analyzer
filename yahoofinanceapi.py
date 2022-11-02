import yfinance as yf
import pandas as pd
​
tickers_list = ['MRNA', 'XPO', 'ICE', 'GILD']
#Column names for dataframe *must parallel the api_col_list
df_col_list = ['Ticker', 'Company Name', 'Sector']
#List of JSON keys from Yahoo Finance API
api_col_list = ['symbol', 'longName', 'sector']
​
​
def getCompanyInfo(tickers, df_cols, api_cols):
    complete_list = [] #List to hold the lists generated for each row of values that we will use in company_df

    #Loops through each ticker, gets all the information, and pulls the values from the desired feilds in api_col_list
    for symbol in tickers:
        ticker = yf.Ticker(symbol)
        company_info = ticker.info
        val_list = []
​
    #Appends values for each api_column in api_column_list for a ticker and appends them to a list for that ticker
        for api_column in api_cols:
            val_list.append(company_info[api_column])

    #Appends the list of values for a ticker to the complete_list
        complete_list.append(val_list)

    #Generate and print dataframe with lists of ticker values
    company_df = pd.DataFrame(complete_list, columns=df_cols)
    print(company_df)
    pd.company_df.to_csv()

​
getCompanyInfo(tickers_list, df_col_list, api_col_list)
