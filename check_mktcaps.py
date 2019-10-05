import requests
import operator

SYMBOLS = ['AAPL', 'GOOG', 'MSFT', 'AMZN', 'FB', 'ORCL', 'IBM', 'INTC', 'NFLX', 'AMD', 'UBER']

api_key = "sk_002f4d2281de40288916d8eb2ee71217"

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
