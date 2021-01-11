import requests
import operator

from settings import IEXAPIS_API_KEY

SYMBOLS = ['AAPL', 'GOOG', 'MSFT', 'AMZN', 'FB', 'ORCL', 'IBM', 'INTC', 'NFLX', 'AMD', 'UBER']

CRYPTO_SYMBOLS = ['BTCUSD', 'ETHUSD','XLMUSDT', 'DASHUSDT']

api_key = IEXAPIS_API_KEY

def do_check():
    vals = []
    for symbol in SYMBOLS:
        vals.append(requests.get(f'https://cloud.iexapis.com/v1/stock/{symbol}/quote?token={api_key}').json())
    res = {
        x['symbol']: x['marketCap'] for x in vals
    }
    sorted_x = sorted(res.items(), key=operator.itemgetter(1), reverse=True)

    pos = 1
    r = ""
    for stock, mkt_value in sorted_x:
        r += f"{pos:02}.- {stock:5} ===> {mkt_value:>15,}\n"
        pos += 1

    return r


def do_check_crypto():
    vals = []
    for symbol in CRYPTO_SYMBOLS:
        vals.append(requests.get(f'https://cloud.iexapis.com/v1/crypto/{symbol}/price?token={api_key}').json())

    print("GOT VALS")
    print(vals)
    res = {
        x['symbol']: float(x['price']) for x in vals
    }
    print(res)
    sorted_x = sorted(res.items(), key=operator.itemgetter(1), reverse=True)
    print(sorted_x)

    pos = 1
    r = ""
    for stock, mkt_value in sorted_x:
        r += f"{pos:02}.- {stock:8} ===> {mkt_value:>15.4f}\n"
        pos += 1

    return r

