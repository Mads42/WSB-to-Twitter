import json



# with open(filename) as fh:
#     for line in fh:
#         command, description = line.strip().split(' ', 1)
#         commands[command] = description.strip()

nasdaqTickers = {}
nasdaq = open("NasdaqTickers.txt")
for line in nasdaq:
    key, value = line.strip().split()
    #nasdaqTickers[key.lower()] = int(value)
    nasdaqTickers[key] = int(value)

#print(nasdaqTickers)

nyseTickers = {}
nyse = open("nyseTickers.txt")
for line in nyse:
    key, value = line.strip().split()
    #nyseTickers[key.lower()] = int(value)
    nyseTickers[key] = int(value)


#print(nyseTickers)

allTickers = {**nasdaqTickers, **nyseTickers}
#print(allTickers)