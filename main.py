import fetcher_plotter as fp

def main():
    stock_name = input('Give LSE: ')
    stock = fp.plotter(stock_name)
    stock.plot()

if __name__ == "__main__":
    main()
