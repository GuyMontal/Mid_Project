import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import json

# A ticker is one stock
tickers = ["msft","aapl"]

#pulling data from api directly into pandas df
for ticker in tickers:
    stockData = yf.Ticker(ticker).history(period = "5d")
    stockDataClose = yf.Ticker(ticker).history(period = "5d").Close
    print(f"The data for {ticker} is:\n {stockData}\n")

