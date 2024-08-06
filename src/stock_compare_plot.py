import matplotlib.pyplot as plt
import yfinance as yf


def stocks_compare_plot(stock_id_name_dict):
    plt.rc('figure', figsize=(10, 5))
    plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei']
    plt.rcParams['axes.unicode_minus'] = False
    for stock_id, stock_name in stock_id_name_dict.items():
        stock = yf.Ticker(stock_id)
        stock_history = stock.history(period="1y")
        dates = stock_history.index
        price = stock_history['Close']
        stock_id_name_str = stock_id + '  ' + stock_name
        # plot lines
        plt.plot(dates, price, label=stock_id_name_str)

    plt.legend()
    plt.show()
