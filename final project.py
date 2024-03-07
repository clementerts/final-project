import yfinance as yf
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

def get_stock_price(ticker):
    current_time = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    stock = yf.Ticker(ticker)
    current_price = stock.history(period='1d')['Close'].iloc[-1]
    return current_price, current_time

def plot_stock_prices(ticker):
    stock = yf.Ticker(ticker)
    hist = stock.history(period='265d')
    plt.plot(hist.index, hist['Close'], label=ticker)
    plt.xlabel('Date')
    plt.ylabel('Price ($)')
    plt.title('Stock Prices Over the Last Year')
    plt.legend()
    plt.grid(True)

def main():
    num_stocks = int(input("Enter the number of stocks you want to retrieve prices for: "))
    tickers = []
    for i in range(num_stocks):
        ticker = input(f"Enter the ticker symbol of stock {i+1}: ")
        tickers.append(ticker)

    for ticker in tickers:
        price, data_time = get_stock_price(ticker)
        print(f"At {data_time}, the current price of {ticker} is ${price}")
        plot_stock_prices(ticker)

    plt.show()
main()
