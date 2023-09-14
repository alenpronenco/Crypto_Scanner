import ccxt.async_support as ccxt
import asyncio
import bybit
from dotenv import load_dotenv
import os
from functools import partial

# Load environment variables from .env file
load_dotenv()

# Extract environment variables
BITFINEX_API_KEY = os.getenv("BITFINEX_API_KEY")
BITFINEX_API_SECRET = os.getenv("BITFINEX_API_SECRET")

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


async def initialize_exchanges():
    exchanges = {
        'Bitfinex': ccxt.bitfinex({
            'apiKey': BITFINEX_API_KEY,
            'secret': BITFINEX_API_SECRET,
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
    await asyncio.gather(*[exchange.load_markets() for exchange in exchanges.values()])
    return exchanges


async def fetch_price(exchange, symbol):
    try:
        ticker = await exchange.fetch_ticker(symbol)
        return float(ticker['last'])
    except Exception as e:
        print(f"An error occurred while fetching {symbol} from {exchange.name}: {e}")
        return None


async def fetch_bybit_price(client, symbol):
    loop = asyncio.get_event_loop()
    try:
        func = partial(client.Market.Market_symbolInfo, symbol=symbol)
        response = await loop.run_in_executor(None, func)

        if response and isinstance(response, tuple) and 'result' in response[0]:
            price = float(response[0]['result'][0].get('last_price', 0))
            return price
        else:
            print(f"Ошибка при получении цены для {symbol} на Bybit: Ответ не содержит ожидаемых данных.")
            return None
    except Exception as e:
        print(f"Ошибка при получении цены для {symbol} на Bybit: {e}")
        return None


async def find_arbitrage_opportunities(exchanges, coins):
    opportunities = []

    for coin in coins:
        for exchange1_name, exchange1 in exchanges.items():
            for exchange2_name, exchange2 in exchanges.items():
                if exchange1_name != exchange2_name:
                    symbol1 = coins[coin]
                    symbol2 = coins[coin]

                    price1 = await fetch_price(exchange1, symbol1)
                    price2 = await fetch_price(exchange2, symbol2)

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

    sorted_opportunities = sorted(opportunities, key=lambda x: x['Profit Percentage'], reverse=True)

    print("\nArbitrage Opportunities:")
    for opportunity in sorted_opportunities:
        print(f"Coin: {opportunity['Coin']}")
        print(f"Buy on {opportunity['Buy Exchange']} at {opportunity['Buy Price']}")
        print(f"Sell on {opportunity['Sell Exchange']} at {opportunity['Sell Price']}")
        print(f"Profit Percentage: {opportunity['Profit Percentage']:.2f}%\n")


async def main():
    exchanges = await initialize_exchanges()

    coins = {
        'BTC': 'BTC/USDT',
        'ETH': 'ETH/USDT',
        'LTC': 'LTC/USDT',
        'BNB': 'BNB/USDT',
        'USDC': 'USDC/USDT',
        'XRP': 'XRP/USDT',
        'ADA': 'ADA/USDT',
        'DOGE': 'DOGE/USDT',
    }

    for coin, symbol in coins.items():
        prices = {}
        print(f"\n{coin} Prices:")

        for name, exchange in exchanges.items():
            price = await fetch_price(exchange, symbol)
            if price:
                prices[name] = price
                print(f"{name}: {price}")

        bybit_client = bybit.bybit(test=False, api_key=BYBIT_API_KEY, api_secret=BYBIT_API_SECRET)

        # Change the following line:
        bybit_symbol = f"{coin}USDT"

        bybit_price = await fetch_bybit_price(bybit_client, bybit_symbol)
        if bybit_price:
            prices['Bybit'] = bybit_price
            print(f"Bybit: {bybit_price}")

        if prices:
            min_price = min(prices.values())
            max_price = max(prices.values())
            print(f"Minimum {coin} Price: {min_price}")
            print(f"Maximum {coin} Price: {max_price}")

    arbitrage_opportunities = await find_arbitrage_opportunities(exchanges, coins)

    # Print the list of arbitrage opportunities to the screen
    print_arbitrage_opportunities(arbitrage_opportunities)

    # Close all exchanges
    for exchange in exchanges.values():
        await exchange.close()


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())