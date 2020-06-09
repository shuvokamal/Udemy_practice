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



