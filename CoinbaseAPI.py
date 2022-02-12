from coinbase.wallet.client import Client
fileName="API.txt"
with open(fileName) as f:
    content=f.read().splitlines()
lines=[]
for line in content:
    lines.append(line)
api_key =lines[3]
api_secret=lines[4]
client = Client(api_key, api_secret)
accounts = client.get_accounts()
CoinBaseWallets=open("CoinBaseWallets.txt","w")
for wallet in accounts.data:
    balance=str( wallet['native_balance']).replace('USD','')
    if(balance!=' 0.00'):
        name=str(wallet['name'])
        end=len(name)
        end=end-7
        name=name[:end]
        CoinBaseWallets.write(name)
        CoinBaseWallets.write('\n')
        CoinBaseWallets.write(balance[1:])
        CoinBaseWallets.write('\n')










# for wallet in accounts.data:
#     message.append( str(wallet['name']) + ' ' +   str(wallet['native_balance']) )
#     value = str( wallet['native_balance']).replace('USD','')
#     total += float(value)
# message.append( 'Total Balance: ' + 'USD ' + str(total) )
# print ( '\n'+message )