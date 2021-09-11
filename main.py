import yfinance as yf
import matplotlib.pyplot as plt


def main():
    stock_name = input('Give name of stock to plot: ') # for trial purposes need to make adaptive later
    stock_ticker = yf.Ticker(stock_name)
    stock_ticker.info
    history = stock_ticker.history(period = "max")

    plt.plot(history['High'])
    plt.plot(history['Low'])
    plt.show()

if __name__ == "__main__":
    main()
