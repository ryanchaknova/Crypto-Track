import gemini

fileName="API.txt"
with open(fileName) as f:
    content=f.read().splitlines()
lines=[]
for line in content:
    lines.append(line)
api_key =lines[9]
api_secret=lines[10]
r = gemini.PrivateClient(api_key, api_secret)
get_balance= r.get_balance()
assert type(get_balance) is list
i=0
GeminiDataWrite=open("GeminiData.txt","w")
for x in get_balance:  
    curr=get_balance[i]['currency']
    bal=get_balance[i]['amount']
    GeminiDataWrite.write(curr)
    GeminiDataWrite.write("\n")
    GeminiDataWrite.write(bal)
    GeminiDataWrite.write("\n")
    i=i+1