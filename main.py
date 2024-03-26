import yfinance as yf
import pandas as pd
import utils

# A ticker is one stock
tickers = ['NVDA','ARM']

#Data manipulation

# Selecting relevant columns from the data frame and scaling them 
df_close_prices = yf.download(tickers, period = "6mo")['Close']
df_volumes = yf.download(tickers, period = "6mo")['Volume']
scalled_close_prices = df_close_prices / df_close_prices.iloc[0,:]
scalled_volumes = df_volumes / df_volumes.iloc[0,:]

#calculations and cleaning NAN values due to missing data

# Calculating the daily change in precentages
df_daily_returns = (df_close_prices.pct_change()* 100).fillna(0)
#calculating RSI measure which used for over/under bought 
df_rsi_result = utils.calculate_rsi(df_close_prices).fillna(0)



#Visualization


# Plotting close prices for all stocks 
utils.plotShow(scalled_close_prices, "Closing Prices", "Date", "Price")

#Plotting volume for each stock
utils.plotShow(scalled_volumes, "Volumes Traded", "Date", "Volume")

# Plotting daily change
utils.plotShow(df_daily_returns, "Daily Returns", "Date", "Change in %")

#Plotting RSI measure for each stock
utils.plotShow(df_rsi_result, "RSI measure", "Date", "RSI")