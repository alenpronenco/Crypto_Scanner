import bybit
import ccxt
from binance.client import Client

# Ваши API-ключи для Binance
binance_api_key = '8Jr4apdeC8xtzVuBKOkCZGLxZmfhORHG20MM3QvZhPTESYQqTXxf0RqtpwMR0ld4'
binance_api_secret = 'nRz9ZggQlADIiCRNEYxoYmwHrRC79TbXHzP2mqnHFyC9LUNKyPF5BZQaIffriEa4'

# Ваши API-ключи для Bittrex (если у вас есть)
bittrex_api_key = '68b8ca137c354aff85fd94c7cbc1d399'
bittrex_api_secret = 'a51743c8172945ac8595c0cbe6f96de4'

# Ваши API-ключи для OKEx (если у вас есть)
okex_api_key = '7d5f4233-94a9-4ae8-916d-700e50217b0b'
okex_api_secret = 'CFC12BB22AC6ADA5AAADA32D2608ADAE'

# Ваши API-ключи для Bybit (если у вас есть)
bybit_api_key = 'ZVbTV5Y2Qfs7DN6AqU'
bybit_api_secret = 'vwlAg6gxat1He0GlbBkoSOZKzPRO2VDCxRJ8'

# Ваши API-ключи для Huobi (если у вас есть)
huobi_api_key = 'e7b0e197-hrf5gdfghe-4f597ee4-8189b'
huobi_api_secret = '5be767c9-c39ea4d5-7339eeb0-b3f38'

# Ваши API-ключи для Gate.io (если у вас есть)
gateio_api_key = '314ba6cbe70616d96a2d1656d4d3e7f5'
gateio_api_secret = '6a655b434094d7e9d8535ba23d0faec990d90d4e5ab00287aea845e2e7472dfb'

# Ваши API-ключи для KuCoin (если у вас есть)
kucoin_api_key = '64f744ab5b0dcc000107c08e'
kucoin_api_secret = '9a054f88-31a8-4388-8ccb-a7fd03af7890'
kucoin_api_passphrase = '168168'

# Создаем экземпляр клиента Kraken
client_kraken = ccxt.kraken()

# Создаем экземпляр клиента Poloniex
client_poloniex = ccxt.poloniex()

# Создаем экземпляр клиента Binance
client_binance = Client(binance_api_key, binance_api_secret)

# Создаем экземпляр клиента Bittrex
client_bittrex = ccxt.bittrex({
    'apiKey': bittrex_api_key,
    'secret': bittrex_api_secret,
    'enableRateLimit': True,
})

# Получаем цену на BTC с Kraken
btc_ticker_kraken = 'BTC/USD'
ticker = client_kraken.fetch_ticker(btc_ticker_kraken)
btc_price_kraken = float(ticker['last'])

# Получаем цену на BTC с Poloniex
btc_ticker_poloniex = 'BTC/USDT'
ticker = client_poloniex.fetch_ticker(btc_ticker_poloniex)
btc_price_poloniex = float(ticker['last'])

# Создаем экземпляр клиента OKEx
client_okex = ccxt.okex({
    'apiKey': okex_api_key,
    'secret': okex_api_secret,
    'enableRateLimit': True,
})

# Создаем экземпляр клиента KuCoin
client_kucoin = ccxt.kucoin({
    'apiKey': kucoin_api_key,
    'secret': kucoin_api_secret,
    'password': kucoin_api_passphrase,
    'enableRateLimit': True,
})

# Создаем экземпляр клиента Gate.io
client_gateio = ccxt.gateio({
    'apiKey': gateio_api_key,
    'secret': gateio_api_secret,
    'enableRateLimit': True,
})

# Создаем экземпляр клиента Bybit
client_bybit = bybit.bybit(test=False, api_key=bybit_api_key, api_secret=bybit_api_secret)

# Создаем экземпляр клиента Huobi
client_huobi = ccxt.huobi({
    'apiKey': huobi_api_key,
    'secret': huobi_api_secret,
    'enableRateLimit': True,
})

# Получаем цену на BTC с Binance
btc_ticker_binance = 'BTCUSDT'
btc_price_binance = float(client_binance.get_symbol_ticker(symbol=btc_ticker_binance)['price'])

# Получаем цену на BTC с Bittrex
btc_ticker_bittrex = 'BTC/USDT'
btc_price_bittrex = float(client_bittrex.fetch_ticker(btc_ticker_bittrex)['last'])

# Получаем цену на BTC с OKEx
btc_ticker_okex = 'BTC/USDT'
btc_price_okex = float(client_okex.fetch_ticker(btc_ticker_okex)['last'])

# Получаем цену на BTC с Bybit
btc_ticker_bybit = 'BTCUSD'  # Тикер для BTC/USD на Bybit
response = client_bybit.Market.Market_symbolInfo(symbol=btc_ticker_bybit).result()
btc_price_bybit = float(response[0]['result'][0]['last_price'])

# Получаем цену на BTC с Huobi
btc_ticker_huobi = 'BTC/USDT'
btc_price_huobi = float(client_huobi.fetch_ticker(btc_ticker_huobi)['last'])

# Получаем цену на BTC с KuCoin
btc_ticker_kucoin = 'BTC/USDT'
btc_price_kucoin = float(client_kucoin.fetch_ticker(btc_ticker_kucoin)['last'])

# Получаем цену на BTC с Gate.io
btc_ticker_gateio = 'BTC/USDT'
btc_price_gateio = float(client_gateio.fetch_ticker(btc_ticker_gateio)['last'])

# Получаем цену на ETH с Kraken
eth_ticker_kraken = 'ETH/USD'
ticker = client_kraken.fetch_ticker(eth_ticker_kraken)
eth_price_kraken = float(ticker['last'])

# Получаем цену на ETH с Poloniex
eth_ticker_poloniex = 'ETH/USDT'
ticker = client_poloniex.fetch_ticker(eth_ticker_poloniex)
eth_price_poloniex = float(ticker['last'])

# Получаем цену на ETH с Binance
eth_ticker_binance = 'ETHUSDT'
eth_price_binance = float(client_binance.get_symbol_ticker(symbol=eth_ticker_binance)['price'])

# Получаем цену на ETH с Bittrex
eth_ticker_bittrex = 'ETH/USDT'
eth_price_bittrex = float(client_bittrex.fetch_ticker(eth_ticker_bittrex)['last'])

# Получаем цену на ETH с OKEx
eth_ticker_okex = 'ETH/USDT'
eth_price_okex = float(client_okex.fetch_ticker(eth_ticker_okex)['last'])

# Получаем цену на ETH с Bybit
eth_ticker_bybit = 'ETHUSD'  # Тикер для ETH/USD на Bybit
response = client_bybit.Market.Market_symbolInfo(symbol=eth_ticker_bybit).result()
eth_price_bybit = float(response[0]['result'][0]['last_price'])

# Получаем цену на ETH с Huobi
eth_ticker_huobi = 'ETH/USDT'
eth_price_huobi = float(client_huobi.fetch_ticker(eth_ticker_huobi)['last'])

# Получаем цену на ETH с KuCoin
eth_ticker_kucoin = 'ETH/USDT'
eth_price_kucoin = float(client_kucoin.fetch_ticker(eth_ticker_kucoin)['last'])

# Получаем цену на ETH с Gate.io
eth_ticker_gateio = 'ETH/USDT'
eth_price_gateio = float(client_gateio.fetch_ticker(eth_ticker_gateio)['last'])

# Получаем цену на LTC с Kraken
ltc_ticker_kraken = 'LTC/USD'
ticker = client_kraken.fetch_ticker(ltc_ticker_kraken)
ltc_price_kraken = float(ticker['last'])

# Получаем цену на LTC с Poloniex
ltc_ticker_poloniex = 'LTC/USDT'
ticker = client_poloniex.fetch_ticker(ltc_ticker_poloniex)
ltc_price_poloniex = float(ticker['last'])

# Получаем цену на LTC с Binance
ltc_ticker_binance = 'LTCUSDT'
ltc_price_binance = float(client_binance.get_symbol_ticker(symbol=ltc_ticker_binance)['price'])

# Получаем цену на LTC с Bittrex
ltc_ticker_bittrex = 'LTC/USDT'
ltc_price_bittrex = float(client_bittrex.fetch_ticker(ltc_ticker_bittrex)['last'])

# Получаем цену на LTC с OKEx
ltc_ticker_okex = 'LTC/USDT'
ltc_price_okex = float(client_okex.fetch_ticker(ltc_ticker_okex)['last'])

# Получаем цену на LTC с Bybit
ltc_ticker_bybit = 'LTCUSD'  # Тикер для LTC/USD на Bybit
response = client_bybit.Market.Market_symbolInfo(symbol=ltc_ticker_bybit).result()
ltc_price_bybit = float(response[0]['result'][0]['last_price'])

# Получаем цену на LTC с Huobi
ltc_ticker_huobi = 'LTC/USDT'
ltc_price_huobi = float(client_huobi.fetch_ticker(ltc_ticker_huobi)['last'])

# Получаем цену на LTC с KuCoin
ltc_ticker_kucoin = 'LTC/USDT'
ltc_price_kucoin = float(client_kucoin.fetch_ticker(ltc_ticker_kucoin)['last'])

# Получаем цену на LTC с Gate.io
ltc_ticker_gateio = 'LTC/USDT'
ltc_price_gateio = float(client_gateio.fetch_ticker(ltc_ticker_gateio)['last'])

# Выводим цены на BTC, ETH, LTC
print(f'Kraken BTC Price: {btc_price_kraken}')
print(f'Poloniex BTC Price: {btc_price_poloniex}')
print(f'Binance BTC Price: {btc_price_binance}')
print(f'Bittrex BTC Price: {btc_price_bittrex}')
print(f'OKEx BTC Price: {btc_price_okex}')
print(f'Bybit BTC Price: {btc_price_bybit}')
print(f'Huobi BTC Price: {btc_price_huobi}')
print(f'Gate.io BTC Price: {btc_price_gateio}')
print(f'Kraken ETH Price: {eth_price_kraken}')
print(f'Poloniex ETH Price: {eth_price_poloniex}')
print(f'Binance ETH Price: {eth_price_binance}')
print(f'Bittrex ETH Price: {eth_price_bittrex}')
print(f'OKEx ETH Price: {eth_price_okex}')
print(f'Bybit ETH Price: {eth_price_bybit}')
print(f'Huobi ETH Price: {eth_price_huobi}')
print(f'Gate.io ETH Price: {eth_price_gateio}')
print(f'Kraken LTC Price: {ltc_price_kraken}')
print(f'Poloniex LTC Price: {ltc_price_poloniex}')
print(f'Binance LTC Price: {ltc_price_binance}')
print(f'Bittrex LTC Price: {ltc_price_bittrex}')
print(f'OKEx LTC Price: {ltc_price_okex}')
print(f'Bybit LTC Price: {ltc_price_bybit}')
print(f'Huobi LTC Price: {ltc_price_huobi}')
print(f'Gate.io LTC Price: {ltc_price_gateio}')


# Сравниваем цены и выводим минимальные и максимальные цены для каждой монеты
def print_min_max_prices(coin_name, prices):
    min_price = min(prices)
    max_price = max(prices)
    print(f'Minimum {coin_name} Price: {min_price}')
    print(f'Maximum {coin_name} Price: {max_price}')


# Сравниваем цены и выводим минимальные и максимальные цены
print_min_max_prices('BTC', [btc_price_binance, btc_price_bittrex, btc_price_okex, btc_price_bybit, btc_price_huobi,
                             btc_price_gateio, btc_price_poloniex, btc_price_kucoin, btc_price_kraken])
print_min_max_prices('ETH', [eth_price_binance, eth_price_bittrex, eth_price_okex, eth_price_bybit, eth_price_huobi,
                             eth_price_gateio, eth_price_poloniex, eth_price_kraken])
print_min_max_prices('LTC', [ltc_price_binance, ltc_price_bittrex, ltc_price_okex, ltc_price_bybit, ltc_price_huobi,
                             ltc_price_gateio, ltc_price_poloniex, ltc_price_kraken])
