import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# A ticker is one stock
tickers = ['NVDA']

# Fetch historical data
stocksData = yf.download(tickers, period = "30d")

# Select close prices and volumes
close_prices = stocksData['Adj Close'] #/ stocksData['Adj Close'].mean()
volumes = stocksData['Volume']

# Calculating the daily change in precentages
daily_returns = (close_prices.pct_change()* 100)

close_prices.info()
#volumes.info()
#daily_returns.info()

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
