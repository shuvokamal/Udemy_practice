# open the file and find average closing price:
with open("playway.txt", 'r') as file:
    content = file.read()
    lines = content.splitlines()


close = []
for idx, line in enumerate(lines):
    if idx > 0:
        close.append(int(line.split(',')[-2]))
print(close)

average_amt= sum(close)/len(close)

print(f"The average 3 days closing price is: {average_amt: .2f}")

# make a list of currency pairs with USD symbol
with open ("currencies.txt", 'r') as file:
    content = file.read().splitlines()
words = []
for i in content:
    if 'USD' in i:
        words.append(i)
print(words)

# take date and close column, make a dictionary, write into another file
with open ("playway1.txt", 'r') as file:
    content= file.read().splitlines()

data = [(line.split(',')[0], line.split(',')[4]) for line in content]
result = {
    data[0][0]: [data[1:][i][0] for i in range(len(data) - 1)],
    data[0][1]: [float(data[1:][i][1]) for i in range(len(data) - 1)]
    }
print(result)

#find the max volume
with open ("playway1.txt", 'r') as file:
    content= file.read().splitlines()
values=[]
data = [line.split(',')[-1] for line in content]

for idx, value in enumerate(data):
    if idx > 0:
        values.append(int(value))
print(max(values))

# find the date which give the highest value
with open ("playway1.txt", 'r') as file:
    content= file.read().splitlines()

data = [(line.split(',')[0], line.split(',')[-1]) for line in content][1:]
data = [(val[0], int(val[1])) for val in data]


max_vol = max([val[1] for val in data])
max_date = list(filter(lambda val: val[1] == max_vol, data))[0][0]
print(max_date)

# save all the even numbers in a file, each in a new line:
num = []
for i in range(2,21):
    if i%2==0:
        num.append(i)
with open("num.txt", 'w') as file:
    for even in num:
        file.write(str(even) + '\n')

# save this json file with pretty print, setting indent 4
import json

stocks = {'PLW': ['Playway', 350], 'BBT': ['Boombit', 22]}

with open("sotcks.json", 'w') as file:
    json.dump(stocks,file, indent = 4)

# Two lists given, save them in a csv file
headers = ['user_id', 'amount']
users = [['001', '1400'], ['004', '1300'], ['007', '900']]
with open('adding.text', 'w') as file:
    file.write(','.join(headers) + '\n')
    for user in users:
        file.write(','.join(user) + '\n')