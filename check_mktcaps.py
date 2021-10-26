import requests
import operator
import json

from settings import IEXAPIS_API_KEY, COINMARKETCAP_API_KEY

SYMBOLS = ['AAPL', 'GOOG', 'MSFT', 'AMZN', 'FB', 'ORCL', 'IBM', 'INTC', 'NFLX', 'AMD', 'UBER', 'TSLA', 'NVDA']

#CRYPTO_SYMBOLS = ['BTCUSD', 'ETHUSD','XLMUSD', 'DASHUSD']
CRYPTO_SYMBOLS = ['BTCUSD', 'ETHUSD']

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


def do_check_symbols():
    r = requests.get(f"https://cloud.iexapis.com/stable/ref-data/crypto/symbols?token={api_key}")
    return r.json()


def do_check_crypto_stellar():
    url = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest?slug=stellar"
    headers = {
        "X-CMC_PRO_API_KEY": COINMARKETCAP_API_KEY
    }
    r = requests.get(url, headers=headers)
    return r.json()


def do_check_crypto():
    vals = []
    for symbol in CRYPTO_SYMBOLS:
        vals.append(requests.get(f'https://cloud.iexapis.com/v1/crypto/{symbol}/price?token={api_key}').json())

    print("GOT VALS")

    print(vals)
    res = {
        x['symbol']: float(x['price']) for x in vals
    }

    try:
        stellar = do_check_crypto_stellar()
        res['XLMUSD'] = stellar['data']['512']['quote']['USD']['price']
    except Exception as e:
        print("Can't get STELLAR value: " + str(e))

    print(res)
    sorted_x = sorted(res.items(), key=operator.itemgetter(1), reverse=True)
    print(sorted_x)

    pos = 1
    r = ""
    for stock, mkt_value in sorted_x:
        r += f"{pos:02}.- {stock:8} ===> {mkt_value:>15.4f}\n"
        pos += 1

    return r


#if __name__ == '__main__':
#    s = do_check_crypto()
#    print(json.dumps(s))
    #for sym in s:
    #    if 'XLM' in sym['symbol']:
    #        print(f"{sym['symbol']} -> {sym['name']}")
    #print(do_check_crypto())
