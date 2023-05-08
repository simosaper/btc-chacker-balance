import requests
import time
#Coder: @simosaper11
#channel: @simosaper
# Set the API endpoint for getting the Bitcoin price in USD
ss = input('file bitcoin_addresses: ')
bitcoin_api_url = 'https://api.coindesk.com/v1/bpi/currentprice/USD.json'

response = requests.get(bitcoin_api_url).json()
bitcoin_price_usd = float(response['bpi']['USD']['rate_float'])


with open(ss, 'r') as file:
    # Read the addresses into a list
    bitcoin_addresses = file.read().splitlines()

# Create a dictionary to store the results
results = {}

# Loop through each address and get the balance
for address in bitcoin_addresses:
    response = requests.get(f"https://blockchain.info/q/addressbalance/{address}")
    balance_btc = int(response.text) / 100000000
    balance_usd = balance_btc * bitcoin_price_usd
    # Add the result to the dictionary
    results[address] = {
        'balance_btc': balance_btc,
        'balance_usd': balance_usd
    }
    # Print the result to the console
    print(f"address: {address}, balance: {balance_btc} BTC, ${balance_usd:.2f}")
    # Wait for 2 seconds before processing the next address
    time.sleep(2)

# Save the results to a file
with open('bitcoin_balances.txt', 'w') as file:
    for address, balances in results.items():
        file.write(f"{address}: {balances['balance_btc']} BTC, ${balances['balance_usd']:.2f}\n")
