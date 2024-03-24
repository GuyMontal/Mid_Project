import yfinance as yf
#import pandas as pd
#import matplotlib.pyplot as plt

# A ticker is one stock
tickers = ['NVDA']

# Fetch historical data
df_stocksData = yf.download(tickers, period = "365d")


# Select relevant columns from the data frame
df_close_prices2 = df_stocksData['Close']
print(df_close_prices2.tail(20))
df_close_prices = df_stocksData['Adj Close'] #/ stocksData['Adj Close'].mean()

df_volumes = df_stocksData['Volume']

#calculations
# Calculating the daily change in precentages
df_daily_returns = (df_close_prices.pct_change()* 100)

def calculate_rsi(data, window=14):
   # Calculate price changes
    delta = data.diff()
    
    # Separate positive and negative price changes
    gain = (delta.where(delta > 0, 0)).fillna(0)
    loss = (-delta.where(delta < 0, 0)).fillna(0)
    
    # Calculate average gain and average loss
    avg_gain = gain.rolling(window=window, min_periods=1).mean()
    avg_loss = loss.rolling(window=window, min_periods=1).mean()
    
    # Calculate relative strength (rs)
    rs = avg_gain / avg_loss
    
    # Calculate RSI
    rsi = 100 - (100 / (1 + rs))
    
    return rsi.tail(5)

rsi_result = calculate_rsi(df_close_prices)
print(rsi_result)
#rsi_result.info()
#volumes.info()
#daily_returns.info()


































"""
def plotShow(data_item, title_plt,xlable_plt,ylabel_plt,size = (10, 5)):
        plt.figure(figsize=size)
        data_item.plot()
        plt.title(title_plt)
        plt.xlabel(xlable_plt)
        plt.ylabel(ylabel_plt)
        plt.legend(tickers)
        plt.show()

 
# Plot close prices
plotShow(close_prices, "Close Prices", "Date", "Price")

# Plot volumes
plotShow(volumes, "Volumes Traded", "Date", "Volume")

# Plot daily change
plotShow(daily_returns, "Daily Returns", "Date", "Change")
"""