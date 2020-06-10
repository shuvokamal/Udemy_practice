# find if the extension is xlsx:

filename = '01012020_sales.xlsx'
extension = filename.split('.')[-1]
def truthfinder(x):
    if x == 'xlsx':
        print(True)
    else:
        print(False)
truthfinder(extension)

#another way:
if filename.endswith('xlsx'):
    print(True)
else: print(False)

# check if uppercase
code = 'DSVNDOICSN'
if code.isupper():
    print('Yes')

# check if type is int:
number = 1.0
if isinstance(number, int):
    print('Yes')
else: print('Hell no!')

# check if password is eleven character or too short
password = 'cskdnjcasa!#'
if len(password) >= 11 and '!' in password:
    print('password correct')
else: print('wrong format of password')

# check if an ID is in the list, if not- add it to the list!
project_ids = ['02134', '24253']
project_id = '02135'

if project_id not in project_ids:
    project_ids.append(project_id)

print(project_ids)

# check the project status of ID 02, if it is new, change it to open
project_ids = {
    '01': 'open',
    '02': 'new',
    '03': 'in progress',
    '04': 'completed'
}
if project_ids['02'] == 'new':
    project_ids['02'] = 'open'
    print(project_ids)

# check if the item is in items. If yes, remove it!
item = '001'
items = ['001', '000', '003', '005', '006']
if item in items:
    items.remove(item)
    print(items)

# find the two digits numbers divisible by 11, indivisible by 3, print in console comma separated
result = []
for i in range(10,99):
    if i % 11 == 0 and i % 3 != 0:
        result.append(str(i))
print(','.join(result))

# remove the odd numbers
items = [1, 3, 4, 5, 6, 9, 10, 17, 23, 24]
result = []
for item in items:
    if not item % 2 != 0:
        result.append(item)
print(result)

# another way:

items = [1, 3, 4, 5, 6, 9, 10, 17, 23, 24]
result = []
for i in items:
    if i % 2 == 0:
        result.append(i)
print(result)

# remove the duplicates:
items = [1, 5, 3, 2, 2, 4, 2, 4]
result = []

for i in items:
    if i not in result:
        result.append(i)
print(result)

# take first four words, make them lower, present in a list:
text = 'Python is a very popular programming language'
words = text.lower().split(' ')
print(words[0:4])

# another way:
text = 'Python is a very popular programming language'

words = text.split(' ')
result = []
for idx, word in enumerate(words):
    if idx < 4:
        result.append(word.lower())
print(result)

# from the set, take the values above 0.5
probabilities = [0.21, 0.91, 0.34, 0.55, 0.76, 0.02]
result = []
for i in probabilities:
    if i > 0.5:
        result.append(i)
print(result)

# return 0 if probability is less than 0.5, return 1 if probability is greater than 0.5
probabilities = [0.21, 0.91, 0.34, 0.55, 0.76, 0.02]
result= []
for i in probabilities:
    if i > 0.5:
        result.append(1)
    else: result.append(0)
print(result)

# create a histogram frequency distribution:
items = ['x', 'y', 'z', 'y', 'x', 'y', 'y', 'z', 'x']
freq = {}
for i in items:
    if i not in freq.keys():
        freq[i] = 1
    else: freq[i] += 1
print(freq)

# create a list of words, lower, keep which has letter more than 6, remove punctuation
text = """Python is powerful... and fast
plays well with others
runs everywhere
is friendly & easy to learn
is Open
These are some of the reasons people who use Python would rather not use anything else"""

text= text.lower()
text= text.replace('...', '').replace('\n',' ')
text= text.split(' ')
new_text=[]

for i in text:
    if len(i)>6:
        new_text.append(i)
print(new_text)

#another method:
text = """Python is powerful... and fast
plays well with others
runs everywhere
is friendly & easy to learn
is Open
These are some of the reasons people who use Python would rather not use anything else"""

words = text.split()
words = [word.lower() for word in words]
words = [word.replace('.', '').replace(',', '') for word in words]
words = [word for word in words if len(word) > 6]
print(words)

# select the indexes only with dow and s&p:
indexes = [
    'BOVESPA', 'DOW JONES COMP', 'DOW JONES INDU',
    'DOW JONES TRANS', 'DOW JONES UTIL', 'IPC',
    'IPSA', 'MERVAL', 'NASDAQ COMP', 'NASDAQ100',
    'S&P500', 'S&P/TSX COMP'
]

indexes1 = []
for i in indexes:
    if i.startswith('DOW') or i.startswith('S&P'):
        indexes1.append(i)
print(indexes1)

# another way:
indexes = [
    'BOVESPA', 'DOW JONES COMP', 'DOW JONES INDU',
    'DOW JONES TRANS', 'DOW JONES UTIL', 'IPC',
    'IPSA', 'MERVAL', 'NASDAQ COMP', 'NASDAQ100',
    'S&P500', 'S&P/TSX COMP'
]
for i in indexes:
    if 'DOW' in i or 'S&P' in i:
        print(i)

# iterate through dictionary and print the keys where value greater than 100

gaming = {
    '11B': 362.5,
    'CDR': 297.0,
    'CIG': 0.85,
    'PLW': 318.0,
    'TEN': 300.0
}

for k, v in gaming.items():
    if v > 100:
        print(k)

# check if all elements are letters, those what are only letters, print like "Hello Jack!"
names = ['Jack', 'Leon', 'Alice', '32-3c', 'Bob']

for i in names:
    if i.isalpha():
        print(f"Hi {i}!")

# compare two lists and check if they have at least one common element, if not return False, or return True:
list1 = [1, 2, 0]
list2 = [4, 5, 6, 1]
result = False

for i in list1:
    if i in list2:
        result = True
        break
print(result)

# check if all elements are string, if yes- print True, if not- print False
hashtags = ['holiday', 'sport', 'fit', None, 'fashion']
result = True
for i in hashtags:
    if not isinstance(i, str):
        result = False
        break

print(result)

#check if a number is a prime number:
number = 13
for i in range(2, number):
    if number % i == 0:
        print(f"{number} is not a prime number")
        break

    else: print(f"{number} is a prime number")
    break

#another method:
number = 13

if number > 1:
    for i in range(2, number):
        if number % i == 0:
            print(f'{number} - not a prime number')
            break
    else:
        print(f'{number} - prime number')
else:
    print(f'{number} - not a prime number')
# change USD to PLN, multiply with 40 when changed
gaming = {
    '11B': [362.5, 'PLN'],
    'CDR': [74.25, 'USD'],
    'CIG': [0.85, 'PLN'],
    'PLW': [79.5, 'USD'],
    'TEN': [300.0, 'PLN']
}

for k,v in gaming.items():
    if v[1] == 'USD':
        v[1] = 'PLN'
        v[0] = v[0]*4
print(gaming)

# another way:
gaming = {
    '11B': [362.5, 'PLN'],
    'CDR': [74.25, 'USD'],
    'CIG': [0.85, 'PLN'],
    'PLW': [79.5, 'USD'],
    'TEN': [300.0, 'PLN']
}

for k,v in gaming.items():
    if v[1] == 'PLN':
        continue
    v[1] = 'PLN'
    v[0] = v[0]*4
print(gaming)

#print the names only
names = ['Jack', 'Leon', 'Alice', None, 'Bob']
result= []
for i in names:
    if not isinstance(i, str):
        continue
    result.append(i)
print(result)

#another method:
names = ['Jack', 'Leon', 'Alice', None, 'Bob']

for name in names:
    if name is None:
        continue
    print(name)

# first 10 prime numbers separated by comma by using break

counter = 0
number = 2
prime = []

while counter < 10:
    for i in range(2, number):
        if number % i == 0:
            break
    else:
        prime.append(str(number))
        counter += 1
    number += 1

print(','.join(prime))


# find how long it will take to get the future value
n = 1
pv = 1000
r = 0.04
fv = pv * (1 + r)
while fv <= 2000:
    fv= fv* (1+r)
    n +=1
print(f"future value is {fv: .2f} in {n} years")

#scholastic gradiant descent:
max_iters = 10000
iters = 0
w_0 = -1
previous_step_size = 1
learning_rate = 0.01
precision = 0.000001
derivative = lambda w: 2 * w - 4

while previous_step_size> precision and iters< max_iters:
    w_prev = w_0
    w_0 = w_0 - learning_rate * derivative(w_prev)
    previous_step_size = abs(w_0 - w_prev)
    iters += 1

print(f'A local minimum in point: {w_0:.2f}')

# check if a number in the list:
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
target = 7
start = 0
end = len(numbers) - 1

result= "Not Found"

while start <= end:
    mid = int((start+end)/2)
    if numbers[mid]== target:
        result= "Found"
        break
    else:
        if numbers[mid] < target:
            start = mid + 1
        else: start = mid-1

print(result)

