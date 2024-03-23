import yfinance as yf
import pandas as pd

tickers = ["msft","aapl"]


stocksData = yf.Ticker(tickers[0]).history(period = "1d")

print(stocksData)
