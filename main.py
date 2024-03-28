import yfinance as yf
import utils


# A ticker is one stock
tickers = ['NVDA','ARM', 'MSFT', 'CHAT']

#Data manipulation

# Selecting relevant columns from the pandas data frame  
df_close_prices = yf.download(tickers, period = "6mo")['Adj Close']
df_volumes = yf.download(tickers, period = "6mo")['Volume']

#calculations and cleaning NAN values due to missing data

# Calculating the daily change in precentages for each stock
df_daily_returns = (df_close_prices.pct_change()* 100).fillna(0)
#calculating RSI measure which used for over/under bought 
df_rsi_result = utils.calculate_rsi(df_close_prices).fillna(0)
#calculating the moving avg for each stock with a window of 50 days
df_moving_avg = utils.ma(5, df_close_prices).dropna()

#Scaling some of the pandas series
scalled_close_prices = df_close_prices / df_close_prices.iloc[0,:]
scalled_volumes = df_volumes / df_volumes.iloc[0,:]
scalled_ma = df_moving_avg / df_moving_avg.iloc[0,:]


#Saving the stocks information to a CSV file
df_close_prices.to_csv('Analysis/Closing Prices.csv')
df_daily_returns.to_csv('Analysis/Daily Change.csv')
df_rsi_result.to_csv('Analysis/RSI Measure.csv')
df_moving_avg.to_csv('Analysis/Moving avg.csv')
df_volumes.to_csv('Analysis/Volume.csv')


#Visualization

# Plotting close prices for all stocks 
utils.plotShow(scalled_close_prices, "Closing Prices", "Date", "Price")

#Plotting volume for each stock
utils.plotShow(scalled_volumes, "Volumes Traded", "Date", "Volume")

# Plotting daily change
utils.plotShow(df_daily_returns, "Daily Returns", "Date", "Change in %")

#Plotting RSI measure for each stock
utils.plotShow(df_rsi_result, "RSI measure", "Date", "RSI")

#Plotting the Moving avg for each stock
utils.plotShow(scalled_ma,"Moving avg", "Date", "Moving avg")