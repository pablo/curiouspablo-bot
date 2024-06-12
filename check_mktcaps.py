import requests
import operator
import json

from settings import IEXAPIS_API_KEY, COINMARKETCAP_API_KEY, ALPHAVANTAGE_API_KEY, FINNHUB_API_KEY

SYMBOLS = ['AAPL', 'GOOG', 'MSFT', 'AMZN', 'META', 'ORCL', 'IBM', 'INTC', 'NFLX', 'AMD', 'UBER', 'TSLA', 'NVDA']

CRYPTO_SYMBOLS = [
    'BTC',
    'ETH',
    'XLM',
    'SOL'
]

api_key = IEXAPIS_API_KEY
alphavantage_api_key = ALPHAVANTAGE_API_KEY
finnhub_api_key = FINNHUB_API_KEY

def do_check_iexapis():
    vals = []
    for symbol in SYMBOLS:
        r = requests.get(f'https://cloud.iexapis.com/v1/stock/{symbol}/quote?token={api_key}')
        vals.append(r.json())
    res = {
        x['symbol']: x['marketCap'] for x in vals
    }
    sorted_x = sorted(res.items(), key=operator.itemgetter(1), reverse=True)

    pos = 1
    r = ""
    for stock, mkt_value in sorted_x:
        r += f"{pos:02}.- {stock:5} ===> {mkt_value:>18,0}\n"
        pos += 1


def format_value(mkt_value: float) -> str:
    TN = 1000000000000
    BN = 1000000000
    if mkt_value > TN:
        return f"{mkt_value/TN:>8,.3f} T"
    elif mkt_value > BN:
        return f"{mkt_value/BN:>8,.3f} B"
    else:
        return f"{mkt_value:>8,.3f} M\n"


def do_check():
    vals = []
    for symbol in SYMBOLS:
        r = requests.get(f'https://finnhub.io/api/v1/stock/profile2?symbol={symbol}&token={finnhub_api_key}')
        vals.append(r.json())
    res = {
        x['ticker']: 1000000*x['marketCapitalization'] for x in vals
    }
    sorted_x = sorted(res.items(), key=operator.itemgetter(1), reverse=True)

    pos = 1
    r = ""
    for stock, mkt_value in sorted_x:
        r += f"{pos:02}.- {stock:5} ===> {format_value(mkt_value)}\n"
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
        r += f"{pos:02}.- {stock:3} ===> {mkt_value:>10.4f}\n"
        pos += 1

    return r


if __name__ == '__main__':
    s = do_check()
    print(s)
