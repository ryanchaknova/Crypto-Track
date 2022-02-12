fileName="API.txt"
with open(fileName) as f:
    content=f.read().splitlines()
lines=[]
for line in content:
    lines.append(line)
api_key =lines[15]
api_secret=lines[16]
api_code=lines[17]
from kucoin.client import Client
#IF YOU SEE ERRORS ABOVE...DISREGARD THEM...THE IMPORTS ARE WORKING JUST FINE 
# YOU MUST RUN WITH PYTHON3 COMMAND, THE IMPORTS ARE IN A DIFFERENT SPOT THAN THE IMPORTS USED FOR OG 5 APIS

client = Client(api_key, api_secret,api_code)

accounts=client.get_accounts()
#print(accounts)
KuKoinWallets=open("KukoinWallets.txt","w")
for currency in accounts:
    balance=str(currency['balance'])
    #currency=accounts[3]
    if(balance!='0'):
        name=str(currency['currency'])
        KuKoinWallets.write(name)
        KuKoinWallets.write('\n')
        KuKoinWallets.write(balance)
        KuKoinWallets.write('\n')