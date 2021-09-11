import yfinance as yf
import matplotlib.pyplot as plt


def main():
    stock_name = input('Give LSE: ') # for trial purposes need to make adaptive later
    stock_ticker = yf.Ticker(stock_name)
    stock_ticker.info
    history = stock_ticker.history(period = "max")

    plt.plot(history['High'])
    plt.plot(history['Low'])
    plt.title(stock_name.upper())
    plt.show()

if __name__ == "__main__":
    main()

