import datetime
import time
import requests
import datetime

prices = []

while True:
    try:
        response = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd")
        bitcoin_price = response.json()["bitcoin"]["usd"]
    except KeyError:
        print ("KeyError - No bitcoin found in the response:")
        if response.json()["status"]["error_code"]==429:
            print ("API Rate-Limit exceeded, waiting one minute")
            time.sleep (60)
            continue
        else:
            print ("Unexcpected problem, waiting for one minute.\n Please check response for further info:\n",response.json())
            time.sleep (60)
            continue
    prices.append(bitcoin_price)

    # Print every minute
    print(f"Current Bitcoin Price: {bitcoin_price}$ ({datetime.datetime.now()})")

    # Print 10-minute average -  every 10 minutes
    if len(prices) == 10:
        average_price = sum(prices) / 10
        print(f"10-Minute Average Bitcoin Price: {average_price}$  ({datetime.datetime.now()})")
        prices = []  # Reset the prices list for the next 10-minutes

    time.sleep(60)
