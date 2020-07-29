# open file, delete new line characters, delete the lines that has no characters

with open("gaming.txt",'r') as file:
    text= file.readlines()

a = [line.replace('\n', '') for line in text]
a = [line for line in a if len(line) > 0]

print(a)

# net and tax given, find the gross:

tax = 0.23
net_price = [5.5, 4.0, 9.0, 10.0]
gross = [ round((i + i*tax),2) for i in net_price]
print(gross)

# calculate the future value for different interest rates given:

pv = 1000
n = 10
rate = [0.01, 0.02, 0.03, 0.04, 0.05, 0.06, 0.07]

fv = [round(pv*(1+r)**n,2) for r in rate ]
print(fv)


# find the value of interest

pv = 1000
n = 10
rate = [0.01, 0.02, 0.03, 0.04, 0.05, 0.06, 0.07]
fv = [pv*(1+r)**n for r in rate]
value_of_interest = [round(i-pv, 2) for i in fv]
print(value_of_interest)

# load text, get rid of blank lines, split line in words:
with open('plw.txt', 'r') as file:
    loaded = file.read().splitlines()

loaded = [line for line in loaded if len(line) > 0]
loaded = [word.split() for word in loaded]
print(loaded)

# change upper case t lower, remove punctuation, split in words, take words that has length more than 8 characters

with open('plw.txt', 'r') as file:
    lines = file.read()
    lines = lines.lower().replace(',', '').replace('.', '').split()
    lines = [i for i in lines if len(i) > 7]
    lines = sorted(lines, reverse=True)
    print(lines)

# convert the dictionary to list
data = dict(zip(('a', 'b', 'c', 'd', 'e', 'f'), (1, 2, 3, 4, 5, 6)))
# {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6}
data = [(key, val) for key, val in data.items()]
print(data)

# create a dictionary to map the squares of 1 to 7
result = {i: i**2 for i in range(1, 7)}
print(result)

# make a dictionary that will map the names and the number of characters:
stocks = ['Playway', 'CD Projekt', 'Boombit']
map = {i: len(i) for i in stocks}
print(map)

# map and replace the values with keys:

stocks = {'Boombit': '001', 'CD Projekt': '002', 'Playway': '003'}
map = {(value, key) for key, value in stocks.items() }
print(map)

# dict value greater than 100

stocks = {'Boombit': 22, 'CD Projekt': 295, 'Playway': 350}
map = {key: value for key, value in stocks.items() if stocks[key] > 100}
print(map)

# build a list consisting of dictionaries mapping consecutive digits from 1 to 9
# inclusive to their respective k-th power , for k = 1,2,3

list = [{i:i**j for i in range(1, 10)} for j in range(1, 4)]
print(list)

# make the dictionaries in the following form: {'WIG20': {'number of companies': None,
# 'companies': None, 'cap': None}, 'mWIG40': {'number of companies': None, 'companies': None, 'cap': None}, 'sWIG80':
# {'number of companies': None, 'companies': None, 'cap': None}}

properties = ['number of companies', 'companies', 'cap']
indeks = ['WIG20', 'mWIG40', 'sWIG80']
data = {idx: {i: None for i in properties} for idx in indeks}
print(data)

# list is given, convert it to a dictionary.
indexes = ['WIG20', 'mWIG40', 'WIG80']
dict = {idx: i for i in indexes for idx in range(0, len(indexes)) } # don't work
print(dict) # don't work

# alternative
indexes = ['WIG20', 'mWIG40', 'sWIG80']
data = {key: val for key, val in enumerate(indexes)}
print(data)



