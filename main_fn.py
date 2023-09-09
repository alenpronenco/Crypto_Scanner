import ccxt
from binance.client import Client
import bybit

# Здесь должны быть ваши API-ключи для каждой биржи (изменено на фиктивные ключи)
exchange_settings = {
    'Binance': {'api_key': '8Jr4apdeC8xtzVuBKOkCZGLxZmfhORHG20MM3QvZhPTESYQqTXxf0RqtpwMR0ld4', 'api_secret': 'nRz9ZggQlADIiCRNEYxoYmwHrRC79TbXHzP2mqnHFyC9LUNKyPF5BZQaIffriEa4'},
    'Bittrex': {'api_key': '68b8ca137c354aff85fd94c7cbc1d399', 'api_secret': 'a51743c8172945ac8595c0cbe6f96de4'},
    'OKEx': {'api_key': '7d5f4233-94a9-4ae8-916d-700e50217b0b', 'api_secret': 'FC12BB22AC6ADA5AAADA32D2608ADAE'},
    'Bybit': {'api_key': 'ZVbTV5Y2Qfs7DN6AqU', 'api_secret': 'vwlAg6gxat1He0GlbBkoSOZKzPRO2VDCxRJ8'},
    'Huobi': {'api_key': 'e7b0e197-hrf5gdfghe-4f597ee4-8189b', 'api_secret': '5be767c9-c39ea4d5-7339eeb0-b3f38'},
    'Gateio': {'api_key': '314ba6cbe70616d96a2d1656d4d3e7f5', 'api_secret': '6a655b434094d7e9d8535ba23d0faec990d90d4e5ab00287aea845e2e7472dfb'},
    'KuCoin': {'api_key': '64f744ab5b0dcc000107c08e', 'api_secret': '9a054f88-31a8-4388-8ccb-a7fd03af7890', 'api_passphrase': '168168'},
}

exchange_clients = {}

def get_coin_prices(coin_symbols, exchange_clients):
    coin_prices = {}
    for coin_symbol in coin_symbols:
        coin_prices[coin_symbol] = {}
        for exchange_name, client in exchange_clients.items():
            print(f"Fetching {coin_symbol} from {exchange_name}...")

            try:
                market_symbol = coin_symbol
                
                # Загрузим все поддерживаемые символы для данной биржи
                client.load_markets()

                # Проверяем, поддерживается ли символ на этой бирже
                if market_symbol not in client.symbols:
                    print(f"{exchange_name} does not support {market_symbol}")
                    continue

                ticker = client.fetch_ticker(market_symbol)
                coin_prices[coin_symbol][exchange_name] = float(ticker['last'])
                
            except Exception as e:
                print(f"Failed to fetch {coin_symbol} price from {exchange_name}: {str(e)}")
                
    return coin_prices

# Список монет и их тикеры
coin_symbols = ['BTC/USDT', 'ETH/USDT', 'LTC/USDT']

# Получение цен для монет с разных бирж
coin_prices = get_coin_prices(coin_symbols, exchange_clients)

# Проверим, если coin_prices является None или пустым словарем
if coin_prices:
    for coin_symbol, prices in coin_prices.items():
        print(f'{coin_symbol} Prices:')
        for exchange_name, price in prices.items():
            print(f'{exchange_name}: {price}')
        print('\n')
else:
    print("Failed to fetch any coin prices.")