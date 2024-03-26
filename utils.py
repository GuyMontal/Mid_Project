import matplotlib.pyplot as plt

tickers = ['NVDA','ARM']

def plotShow(data_item, title_plt,xlable_plt,ylabel_plt,size = (1, 1)):
        plt.figure(figsize=size)
        data_item.plot()
        plt.title(title_plt)
        plt.xlabel(xlable_plt)
        plt.ylabel(ylabel_plt)
        plt.legend(list(data_item.columns))
        plt.savefig(f"Analysis/{title_plt}.png")

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

# Calculate the moving average with a set window of days
def ma(window,data):  
    moving_avg_window = window
    return data.rolling(window=moving_avg_window).mean()

