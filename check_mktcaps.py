import requests
import operator
import json

from settings import IEXAPIS_API_KEY, COINMARKETCAP_API_KEY

SYMBOLS = ['AAPL', 'GOOG', 'MSFT', 'AMZN', 'META', 'ORCL', 'IBM', 'INTC', 'NFLX', 'AMD', 'UBER', 'TSLA', 'NVDA']

CRYPTO_SYMBOLS = [
    'BTC',
    'ETH',
    'XLM'
]

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
        r += f"{pos:02}.- {stock:5} ===> {mkt_value:>18,}\n"
        pos += 1

    return r


def do_check_symbols():
    r = requests.get(f"https://cloud.iexapis.com/stable/ref-data/crypto/symbols?token={api_key}")
    return r.json()


def do_check_crypto(symbols):
    url = f"https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest?symbol={','.join(symbols)}"
    headers = {
        "X-CMC_PRO_API_KEY": COINMARKETCAP_API_KEY
    }
    r = requests.get(url, headers=headers)
    return r.json()


def do_check_cryptos():
    vals = do_check_crypto(CRYPTO_SYMBOLS)

    res = {
        k: float(v['quote']['USD']['price']) for k, v in vals['data'].items()
    }

    print(res)
    sorted_x = sorted(res.items(), key=operator.itemgetter(1), reverse=True)
    print(sorted_x)

    pos = 1
    r = ""
    for stock, mkt_value in sorted_x:
        r += f"{pos:02}.- {stock:3} ===> {mkt_value:>5.4f}\n"
        pos += 1

    return r


#if __name__ == '__main__':
#    s = do_check_cryptos()
#    print(json.dumps(s))
    #for sym in s:
    #    if 'XLM' in sym['symbol']:
    #        print(f"{sym['symbol']} -> {sym['name']}")
    #print(do_check_crypto())
