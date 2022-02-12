
import requests
fileName="API.txt"
with open(fileName) as f:
    content=f.read().splitlines()
lines=[]


for line in content:
    lines.append(line)

api_key =lines[1]

headers={
    'X-CMC_PRO_API_KEY' : api_key,
    'Accepts' : 'application/json'

        }

params={
    'start' : '1',
    'limit' : '4000',
    'convert' : 'USD'
}

url='https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'

json = requests.get(url, params=params,headers=headers).json()

coins = json['data']

PriceDataWriteToFile=open("PriceData.txt","w")
for x in coins:
    #print(x['symbol'])
    PriceDataWriteToFile.write(x['symbol'])
    PriceDataWriteToFile.write('\n')
    PriceDataWriteToFile.write( str(x['quote']['USD']['price']))
    PriceDataWriteToFile.write('\n')
