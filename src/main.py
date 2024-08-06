from src.stock_compare_plot import stocks_compare_plot


def taiwanese_memory_ip_stocks_compare():
    stock_id_name_dict = {
        '6531.TW': '世芯',
        '6533.TW': '晶心科',
        '3529.TWO': '力旺',
        '6643.TWO': 'M31',
        '6786.TWO': '芯測'
    }
    stocks_compare_plot(stock_id_name_dict)


if __name__ == '__main__':
    taiwanese_memory_ip_stocks_compare()
