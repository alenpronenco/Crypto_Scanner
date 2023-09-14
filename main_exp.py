import bybit
from dotenv import load_dotenv
import os
import ccxt

# Загрузить переменные окружения из файла .env
load_dotenv()

# Извлечение переменных окружения
BINANCE_API_KEY = os.getenv("BINANCE_API_KEY")
BINANCE_API_SECRET = os.getenv("BINANCE_API_SECRET")

BITRIX_API_KEY = os.getenv("BITRIX_API_KEY")
BITRIX_API_SECRET = os.getenv("BITRIX_API_SECRET")

OKEX_API_KEY = os.getenv("OKEX_API_KEY")
OKEX_API_SECRET = os.getenv("OKEX_API_SECRET")

BYBIT_API_KEY = os.getenv("BYBIT_API_KEY")
BYBIT_API_SECRET = os.getenv("BYBIT_API_SECRET")

HUOBI_API_KEY = os.getenv("HUOBI_API_KEY")
HUOBI_API_SECRET = os.getenv("HUOBI_API_SECRET")

GATEIO_API_KEY = os.getenv("GATEIO_API_KEY")
GATEIO_API_SECRET = os.getenv("GATEIO_API_SECRET")

KUCOIN_API_KEY = os.getenv("KUCOIN_API_KEY")
KUCOIN_API_SECRET = os.getenv("KUCOIN_API_SECRET")
KUCOIN_API_PASSPHRASE = os.getenv("KUCOIN_API_PASSPHRASE")

# Инициализация экземпляров ccxt
exchanges = {
    'Binance': ccxt.binance({
        'apiKey': os.getenv("BINANCE_API_KEY"),
        'secret': os.getenv("BINANCE_API_SECRET"),
        'rateLimit': 2000,
    }),
    'Bitrix': ccxt.bitfinex({
        'apiKey': BITRIX_API_KEY,
        'secret': BITRIX_API_SECRET,
    }),
    'Okex': ccxt.okex({
        'apiKey': OKEX_API_KEY,
        'secret': OKEX_API_SECRET,
    }),
    'Bybit': ccxt.bybit({
        'apiKey': BYBIT_API_KEY,
        'secret': BYBIT_API_SECRET,
    }),
    'Huobi': ccxt.huobipro({
        'apiKey': HUOBI_API_KEY,
        'secret': HUOBI_API_SECRET,
    }),
    'Gateio': ccxt.gateio({
        'apiKey': GATEIO_API_KEY,
        'secret': GATEIO_API_SECRET,
    }),
    'KuCoin': ccxt.kucoin({
        'apiKey': KUCOIN_API_KEY,
        'secret': KUCOIN_API_SECRET,
        'password': KUCOIN_API_PASSPHRASE,
    })
}

# Здесь ваш основной код

def fetch_price(exchange, symbol):
    try:
        ticker = exchange.fetch_ticker(symbol)
        return float(ticker['last'])
    except UnicodeEncodeError as uee:
        print(f"Encoding error while fetching {symbol} from {exchange.name}: {uee}")
        return None
    except Exception as e:
        print(f"An error occurred while fetching {symbol} from {exchange.name}: {e}")
        return None

def fetch_bybit_price(client, symbol):
    try:
        response = client.Market.Market_symbolInfo(symbol=symbol).result()
        return float(response[0]['result'][0]['last_price'])
    except Exception as e:
        print(f"Ошибка при получении цены для {symbol} на Bybit: {e}")
        return None

def find_arbitrage_opportunities(exchanges, coins):
    opportunities = []

    for coin in coins:
        for exchange1_name, exchange1 in exchanges.items():
            for exchange2_name, exchange2 in exchanges.items():
                if exchange1_name != exchange2_name:
                    symbol1 = coins[coin]
                    symbol2 = coins[coin]

                    price1 = fetch_price(exchange1, symbol1)
                    price2 = fetch_price(exchange2, symbol2)

                    if price1 and price2:
                        if price1 < price2:
                            opportunities.append({
                                'Buy Exchange': exchange1_name,
                                'Sell Exchange': exchange2_name,
                                'Coin': coin,
                                'Buy Price': price1,
                                'Sell Price': price2,
                                'Profit Percentage': ((price2 - price1) / price1) * 100
                            })

    return opportunities

def print_arbitrage_opportunities(opportunities):
    if not opportunities:
        print("No arbitrage opportunities found.")
        return

    print("\nArbitrage Opportunities:")
    for opportunity in opportunities:
        print(f"Coin: {opportunity['Coin']}")
        print(f"Buy on {opportunity['Buy Exchange']} at {opportunity['Buy Price']}")
        print(f"Sell on {opportunity['Sell Exchange']} at {opportunity['Sell Price']}")
        print(f"Profit Percentage: {opportunity['Profit Percentage']:.2f}%\n")

def main():
    # Конфигурация API ключей для всех бирж должна быть в отдельном файле или окружении, а не в коде!

    # Инициализация клиентов
    exchanges = {
        'Kraken': ccxt.kraken(),
        'Poloniex': ccxt.poloniex(),
        'Binance': ccxt.binance({'apiKey': 'ВАШ_API_KEY', 'secret': 'ВАШ_API_SECRET'}),
        'Bittrex': ccxt.bittrex({'apiKey': 'ВАШ_API_KEY', 'secret': 'ВАШ_API_SECRET'}),
        'OKEx': ccxt.okex({'apiKey': 'ВАШ_API_KEY', 'secret': 'ВАШ_API_SECRET'}),
        'Huobi': ccxt.huobi({'apiKey': 'ВАШ_API_KEY', 'secret': 'ВАШ_API_SECRET'}),
        'Gate.io': ccxt.gateio({'apiKey': 'ВАШ_API_KEY', 'secret': 'ВАШ_API_SECRET'}),
        'KuCoin': ccxt.kucoin({'apiKey': 'ВАШ_API_KEY', 'secret': 'ВАШ_API_SECRET', 'password': 'ВАШ_PASSWORD'}),
    }

    bybit_client = bybit.bybit(test=False, api_key='ВАШ_API_KEY', api_secret='ВАШ_API_SECRET')

    coins = {
        'BTC': 'BTC/USDT',
        'ETH': 'ETH/USDT',
        'LTC': 'LTC/USDT'
    }

    bybit_symbols = {
        'BTC': 'BTCUSD',
        'ETH': 'ETHUSD',
        'LTC': 'LTCUSD'
    }

    for coin, symbol in coins.items():
        prices = {}
        print(f"\n{coin} Prices:")

        for name, exchange in exchanges.items():
            price = fetch_price(exchange, symbol)
            if price:
                prices[name] = price
                print(f"{name}: {price}")

        bybit_price = fetch_bybit_price(bybit_client, bybit_symbols[coin])
        if bybit_price:
            prices['Bybit'] = bybit_price
            print(f"Bybit: {bybit_price}")

        if prices:
            min_price = min(prices.values())
            max_price = max(prices.values())
            print(f"Minimum {coin} Price: {min_price}")
            print(f"Maximum {coin} Price: {max_price}")

    arbitrage_opportunities = find_arbitrage_opportunities(exchanges, coins)
    print_arbitrage_opportunities(arbitrage_opportunities)

if __name__ == '__main__':
    main()