from os import name
import pandas
from pycoingecko import CoinGeckoAPI
cg = CoinGeckoAPI()
a = cg.get_coins_markets(vs_currency='usd')
b = pandas.DataFrame(z, columns=['name', 'market_cap'])
print(t)