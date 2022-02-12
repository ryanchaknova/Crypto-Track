
from binance.client import Client
fileName="API.txt"
with open(fileName) as f:
    content=f.read().splitlines()
lines=[]


for line in content:
    lines.append(line)

api_key =lines[12]
api_secret=lines[13]

client = Client(api_key, api_secret,tld='us')


import time
import win32api
gt = client.get_server_time()
tt=time.gmtime(int((gt["serverTime"])/1000))
win32api.SetSystemTime(tt[0],tt[1],0,tt[2],tt[3],tt[4],tt[5],0)


BinanceWrite=open("BinanceData.txt","w")
#the following names list must be updated
names=["BTC","ETH","ZIL","BNB","VET","USDT","ENJ","VTHO","ONE","XLM","ADA","LTC","BUSD","HNT","DOGE","EGLD","HBAR","OMG","SOL","BAT","STORJ","ALGO","ZRX","LINK","XTZ","MATIC","EOS","USDC","MANA","RVN","UNI","KNC","WAVES","BCH","IOTA","ICX","ATOM","QTUM","OXT","BAND","REP","ETC","ONT","ZEC","NEO","COMP","NANO","MKR","DASH","ZEN","DAI","PAXG"]
#print(balance['free']) # THIS IS HOW TO GET THE ACTUAL AMOUNT FROM THE CLINET RETURN
i=0
for x in names:
    name=client.get_asset_balance(asset=names[i])
    bal=name['free']
    if(bal!="0.00000000"):
        BinanceWrite.write(names[i])
        BinanceWrite.write("\n")
        BinanceWrite.write(bal)
        BinanceWrite.write("\n")
    i=i+1