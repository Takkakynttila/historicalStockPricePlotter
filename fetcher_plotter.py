import yfinance as yf
import matplotlib.pyplot as plt

class plotter():
    def __init__(self, stock_lse, period = 'max'): # initiate class with parameters and create required ticker(s) for yfinance
        self.lse = stock_lse
        self.period = period
        self.ticker = yf.Ticker(self.lse)
        self.ticker.info
        self.history = self.ticker.history(period = self.period)

    def plot(self): #plot with high and low prices
        plt.plot(self.history['High'])
        plt.plot(self.history['Low'])
        plt.title(self.lse.upper() + ', ' + self.period)
        plt.show()

