import fetcher_plotter as fp

def main():
    stock_name = input('Give LSE: ')
    stock_period = input('Give optional period (1d, 5d, 1mo, 3mo, 6mo, 1y, 2y, 5y, 10y, ytd, max) - max by default: ')
    if stock_period == None:
        stock = fp.plotter(stock_name)
    else:
        stock = fp.plotter(stock_name, stock_period)

    stock.plot()

if __name__ == "__main__":
    main()

