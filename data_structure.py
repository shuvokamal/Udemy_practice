# add another subject
subjects = {'mathematics', 'biology'}
subjects.add('English') # this is a set object, so add instead of append
print(subjects)

text = 'Programming in python.'
#make lowercase
text= text.lower()
print(text)
# replace space and periods
text= text.replace(' ','').replace('.','')
print(text)

#make a set of individual letters
letters= set(text)
print(f" set is: {text}")

# find which are NOT vowels
vowels = {'a', 'e', 'i', 'o', 'u'}
consonants = letters.difference(vowels)
print(f"Number of consonants: {len(consonants)}")

# symmetric differences. Symmetric difference mean a set that is made of elements which are not common in both sets

A = {2, 4, 6, 8}
B = {4, 10}
sym_diff = A.symmetric_difference(B)
print(f"symmetric difference set is: {sym_diff}")

# another difference example:
ad1_id = {'001', '002', '003'}
ad2_id = {'002', '003', '007'}

bought_once = ad1_id.symmetric_difference(ad2_id)
print(f"The IDs who bought once are: {bought_once}")

# find if those who clicked, has bought or not!
is_clicked = {'9001', '9002', '9005'}
is_bought = {'9002', '9004', '9005'}
result = is_clicked.intersection(is_bought)
print(f"Following IDs are what clicked and bought: {result}")

# combine two tuples:
dji1 = ('AAPL.US', 'IBM.US', 'MSFT.US')
dji2 = ('HD.US', 'GS.US', 'NKE.US')
result = dji1+dji2
print(result)

# Nest the objects in to one tuple:
dji1 = ('AAPL.US', 'IBM.US', 'MSFT.US')
dji2 = ('HD.US', 'GS.US', 'NKE.US')
result = (dji1,dji2)
print(result)

# insert a tuple element between two elements:
members = (('Kate', 23), ('Tom', 19))
members = (members[0], ('shuvo', 25), members[1])
print(members)

# tuple object is given. find the number of occurrences
default = ('YES', 'NO', 'NO', 'YES', 'NO')
print(f"Number of yes: {default.count('YES')}")
print(f"Number of yes: {default.count('NO')}")

# sort the tuple object
names = ('Monica', 'Tom', 'John', 'Michael')
sorted_names = tuple(sorted(names))
print(sorted_names)

# sort the tuples based on values both in ascending and descending order:
info = (('Monica', 19), ('Tom', 21), ('John', 18))
asc = tuple(sorted(info, key=lambda item: item[0])) #sort by name
desc = tuple(sorted(info, key=lambda item: item[1], reverse=True)) # sort by age reverse
print(f'Ascending: {asc}')
print(f'Descending: {desc}')

# Extract an element
stocks = (('Apple Inc', ('AAPL.US', 310)), ('Microsoft Corp', ('MSFT.US', 184)))
print(f"The apple SEC name is: {stocks[0][1][0]}")

## LIST
#add an item to the list:
cities = ['Los Angeles', 'New York', 'Chicago']
cities.append("Miami")
print(cities)

# count the occurence:
idx = ['001', '002', '001', '003', '001']
print(f"The number of occurence of 001 is: {idx.count('001')}")

# make lower case, then make a list of all individual characters, then sort:
text = 'Python programming'
text= text.lower().replace(' ', '')
character= list(set(text))
character=sorted(character, reverse=True)
print(character)

#another method:
text = 'Python programming'
text= text.lower()
character= list(set(text))
character.remove(' ')
character.sort()
print(character)

# Add entries to the list:
filenames = ['view.jpg', 'bear.jpg', 'ball.png']
filenames[0]= 'www.lmg' # replace the first entry with the new one
print(filenames)

filenames.insert(0,'abc.fig') # insert in a particular location, have all the entries including new and old one's
print(filenames)
filenames.remove('ball.png') # remove a particular entry
print(filenames)

# add two lists:
day1 = ['3984', '9042', '4829', '2380']
day2 = ['4231', '5234', '1345', '2455']
print(day1 + day2)

# another way: day1 consisting day2 list too:
day1.extend(day2)
print(day1) # gives same result, but falls under day1 variable

# tuple objects are given, sort them from a to z:
techs = ('python', 'java', 'sql', 'aws')
techs= tuple(sorted(techs))
print(techs)

# list given, combine them with # in the middle:
hashtags = ['summer', 'time', 'vibes']
print('#'.join(hashtags))

## DICTIONARY
## create a dictionary from the data pairs:
capitals = {
    'USA': 'Washington',
    'Germany': 'Berlin',
    'Austria': 'Vienna'
    }
print(capitals)

# extract all keys from the given dictionary:
print(capitals.keys())
# print values of dictionary:
print(capitals.values())
#print both key value pairs:
print(capitals.items())

# extract the value of austria using get() method:
print(capitals.get('Austria'))

# extract value for key AAPL.US
stocks = {
    'MSFT.US': {'Microsoft Corp': 184},
    'AAPL.US': {'Apple Inc': 310},
    'MMM.US': {'3M Co': 148}
}
print(stocks.get('AAPL.US'))
# another method:
print(stocks['AAPL.US'])

# extract the value for Microsoft Corp key
print(stocks['MSFT.US']['Microsoft Corp'])

# update the price of microsoft to 190:
stocks['MSFT.US']['Microsoft Corp'] = 190
print(stocks)
print(stocks['MSFT.US'])

#add another pair:

stocks[3]= {'MUMT.UK': {'mmth':185}}
print(stocks)

# another way
stocks['ABY']= {'abnt':185}
print(stocks)
print(stocks.values())

# transform a list in to two elements tuple object: (ENUMERATE)
tickers = [
    'AAPL.US', 'AXP.US', 'BA.US', 'CAT.US',
    'CSCO.US', 'CVX.US', 'DIS.US', 'DOW.US',
    'GS.US', 'HD.US', 'IBM.US', 'INTC.US'
]

print(list(enumerate(tickers)))

# transform into dictionary (key,value)
print(dict(enumerate(tickers)))

# sort the dictionary:
project_ids = {
    '01': 'open',
    '03': 'in progress',
    '05': 'in progress',
    '04': 'completed'
}
result= list(set(project_ids.values()))
result.sort(reverse=True)
print(result)