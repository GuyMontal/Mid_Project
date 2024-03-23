import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# A ticker is one stock
tickers = ['NVDA','ARM']

# Fetch historical data
stocksData = yf.download(tickers, period = "1mo")

# Select close prices and volumes
close_prices = stocksData['Adj Close'] / stocksData['Adj Close'].mean()
volumes = stocksData['Volume']

# Plot close prices
plt.figure(figsize=(10, 10))
close_prices.plot()
plt.title('Close Prices')
plt.xlabel('Date')
plt.ylabel('Price')
plt.legend(tickers)
#plt.show()

# Plot volumes
plt.figure(figsize=(10, 5))
volumes.plot()
plt.title('Volumes Traded')
plt.xlabel('Date')
plt.ylabel('Volume')
plt.legend(tickers)
#plt.show()

# Calculate daily returns
daily_returns = close_prices.pct_change()

# Plot daily returns
plt.figure(figsize=(10, 5))
daily_returns.plot()
plt.title('Daily Returns')
plt.xlabel('Date')
plt.ylabel('Return')
plt.legend(tickers)
#plt.show()
