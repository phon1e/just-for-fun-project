import requests
res = requests.get('https://api.coinmarketcap.com/v1/ticker/bitcoin/')
data = res.json()
print("1 "+data[0]['symbol']+ " = " +data[0]['price_usd']+" USD")
thb = 31.61*float(data[0]['price_usd'])
print("THB = "+ str(thb)+" Bath")
