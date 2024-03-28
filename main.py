import yfinance as yf
import utils
import argparse


# A ticker is one stock
#tickers = ['NVDA','ARM', 'MSFT', 'CHAT']
def run_all(tickers,period):
        #Data manipulation

        # Selecting relevant columns from the pandas data frame  
        df_close_prices = yf.download(tickers, period)['Adj Close']
        df_volumes = yf.download(tickers, period)['Volume']

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
        df_close_prices.to_csv('Closing Prices.csv')
        df_daily_returns.to_csv('Daily Change.csv')
        df_rsi_result.to_csv('RSI Measure.csv')
        df_moving_avg.to_csv('Moving avg.csv')
        df_volumes.to_csv('Volume.csv')

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

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Stocks")
    parser.add_argument("--target_stocks", type=list, help="The stocks you want to analyze")
    parser.add_argument("--Period", type=str, help="How long back")

    
    args = parser.parse_args()
    run_all(tickers = args.target_stocks,
            period = args.period)