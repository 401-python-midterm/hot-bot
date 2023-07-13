import requests
import datetime
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from modules.investment_recommendation import get_investment_recommendation
from modules.historical_getter import get_historical_data
from modules.current_price  import get_current_price
from rich.console import Console
console = Console()

# Read the API key from api_key.txt file
with open('api_key.txt', 'r') as file:
    api_key = file.read().strip()
headers = {
    "CB-ACCESS-KEY": api_key,
}

# Read the API key from gpt_key.txt file
with open('gpt_api.txt', 'r') as file:
    gpt_api = file.read().strip()

# Retrieve current prices for BTC-USD and ETH-USD
btc_usd_price = get_current_price("BTC-USD", headers)
eth_usd_price = get_current_price("ETH-USD", headers)

# Print current prices
# print("BTC-USD price:", btc_usd_price)
# print("ETH-USD price:", eth_usd_price)

# Historical chart code (including API information)
api_url = "https://api.pro.coinbase.com/products"

# Calculate the start and end dates
end_date = datetime.datetime.now()
start_date = end_date - datetime.timedelta(days=60)


# Retrieve historical data for BTC-USD
btc_data = get_historical_data("BTC-USD", api_url, start_date, end_date)
btc_timestamps = [mdates.date2num(datetime.datetime.fromtimestamp(int(entry[0]))) for entry in btc_data]
btc_opens = [entry[3] for entry in btc_data]
btc_highs = [entry[2] for entry in btc_data]
btc_lows = [entry[1] for entry in btc_data]
btc_closes = [entry[4] for entry in btc_data]

# Retrieve historical data for ETH-USD
eth_data = get_historical_data("ETH-USD",api_url, start_date, end_date)
eth_timestamps = [mdates.date2num(datetime.datetime.fromtimestamp(int(entry[0]))) for entry in eth_data]
eth_opens = [entry[3] for entry in eth_data]
eth_highs = [entry[2] for entry in eth_data]
eth_lows = [entry[1] for entry in eth_data]
eth_closes = [entry[4] for entry in eth_data]

# Plotting Bitcoin (BTC-USD) and Ethereum (ETH-USD) charts
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8))

ax1.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
ax1.xaxis.set_major_locator(mdates.MonthLocator())
ax1.plot(btc_timestamps, btc_closes, color='blue')
ax1.vlines(btc_timestamps, btc_lows, btc_highs, color='black', linewidth=1)
ax1.set_title("Bitcoin (BTC-USD) - 60 Day Historical Data")
ax1.set_xlabel("Date")
ax1.set_ylabel("Price (USD)")
ax1.tick_params(axis='x', rotation=45)

ax2.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
ax2.xaxis.set_major_locator(mdates.MonthLocator())
ax2.plot(eth_timestamps, eth_closes, color='green')
ax2.vlines(eth_timestamps, eth_lows, eth_highs, color='black', linewidth=1)
ax2.set_title("Ethereum (ETH-USD) - 60 Day Historical Data")
ax2.set_xlabel("Date")
ax2.set_ylabel("Price (USD)")
ax2.tick_params(axis='x', rotation=45)

plt.tight_layout()
#plt.show()


def gpt_60(option):
    investment_recommendation = get_investment_recommendation(btc_data, eth_data, btc_opens, btc_highs, btc_lows,   btc_closes, eth_opens, eth_highs, eth_lows, eth_closes, gpt_api, option)

    # Print investment recommendation
    print("Investment Recommendation:", investment_recommendation)  
    console.print('Press "enter" to exit')