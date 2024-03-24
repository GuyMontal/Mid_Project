import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt


def plotShow(data_item, title_plt,xlable_plt,ylabel_plt,size = (10, 5)):
        plt.figure(figsize=size)
        data_item.plot()
        plt.title(title_plt)
        plt.xlabel(xlable_plt)
        plt.ylabel(ylabel_plt)
        plt.legend(tickers)
        plt.savefig(f"{title_plt}.png")

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
    
    return rsi
 

# A ticker is one stock
tickers = ['NVDA','ARM','AMD','MSFT']

#Data manipulation

# Selecting relevant columns from the data frame and scaling them 
df_close_prices = yf.download(tickers, period = "6mo")['Close']
df_volumes = yf.download(tickers, period = "6mo")['Volume']
scalled_close_prices = df_close_prices / df_close_prices.iloc[0,:]
scalled_volumes = df_volumes / df_volumes.iloc[0,:]

#calculations
# Calculating the daily change in precentages
df_daily_returns = (df_close_prices.pct_change()* 100).fillna(0)

df_rsi_result = calculate_rsi(df_close_prices).fillna(0)



#Visualization


# Plotting close prices for all stocks 
plotShow(scalled_close_prices, "Closing Prices", "Date", "Price")

#Plotting volume for each stock
plotShow(scalled_volumes, "Volumes Traded", "Date", "Volume")

# Plotting daily change
plotShow(df_daily_returns, "Daily Returns", "Date", "Change in %")

#Plotting RSI measure for each stock
plotShow(df_rsi_result, "RSI measure", "Date", "RSI")