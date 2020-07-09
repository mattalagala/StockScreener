import pandas as pd
import numpy as np
import yfinance as yf
import datetime as dt
from pandas_datareader import data as pdr

# Workaround for yahoo finance pandas integration
yf.pdr_override()

# Get ticker
stock = input("Enter ticker: ")
print(stock)

# Start of data timeframe
startyear = 2020
startmonth =1
startday=1

start = dt.datetime(startyear, startmonth, startday)

now = dt.datetime.now()

df=pdr.get_data_yahoo(stock, start, now)



#Moving Averages
ma=50

smaString="Sma_"+str(ma)

df[smaString]=df.iloc[:,4].rolling(window=ma).mean()


df=df.iloc[ma:]

numH=0
numC=0

for i in df.index:
    if(df["Adj Close"][i]>df[smaString][i]):
        print("Closed Higher")
        numH+=1
    else: 
        print("Closed Lower")
        numC+=1

print(str(numH))
print(str(numC))