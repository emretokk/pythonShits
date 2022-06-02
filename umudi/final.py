rates = []
words = []
currencyIncrease = []

def read():
	f = open("currency.txt", "r")
	for line in f:
		rates.append(line[0:-2])
	f.close()
read()

if "" in rates:
	rates.remove("")
curRates = []
for currency in rates:
	words = rates[0].split()
	words = words[1:]
	curRate = 0.0
	current = 0
	for cur in words:
		if current !=  len(words)-1:
			curRateNew = float(words[current+1]) - float(words[current])
			if curRateNew > curRate:
				curRate = curRateNew
		current += 1
	curRates.append(curRate)

print(curRates)