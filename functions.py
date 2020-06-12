# evaluate the function:
x = -1.5
expression = 'x**2 + x'
print(eval(expression))

# check if they are tuple
var1 = 'Python'
var2 = ('Python')
var3 = ('Python',)
var4 = ['Python']
var5 = {'Python'}

print(isinstance(var1, tuple))
print(isinstance(var2, tuple))
print(isinstance(var3, tuple))
print(isinstance(var4, tuple))
print(isinstance(var5, tuple))

# find min and max of the alpha
characters = ['k', 'b', 'c', 'j', 'z', 'w']
print(f"First {min(characters)}")
print(f"Last {max(characters)}")

# create a list containing of tuple objects, connects two lists
ticker = ('TEN', 'PLW', 'CDR')
full_name = ('Ten Square Games', 'Playway', 'CD Projekt')
print(list(zip(ticker, full_name)))

# vrify if all the elements returns true
items = (' ', '0', 0.1, True)
print(all(items))

# verify if any object return boolean value False
items = ('', 0.0, 0, False)
print(any(items))
# count the number of 1 in the binary representation
number = 234
binary = bin(number)
binary = binary[2:]
print(binary.count('1'))


# write a method that returns maximum
def maximum(a, b):
    if a > b:
        print(a)
    else:
        print(b)


maximum(4, 2)


# write a method that returns maximum of three numbers
def maxi(a, b, c):
    if a >= b and a >= c:
        print(a)
    elif b >= c:
        print(b)
    else:
        print(c)


maxi(8, 10, 9)


# write a method that takes list or tuple and return the products of all elements
def multi(numbers):
    result = 1
    for i in numbers:
        result *= i
    print(result)


list2 = [2, 4, 10]
multi(list2)


# write a function that will accept a word list and return the length of highest word
def map_longest(words):
    length = []
    for i in words:
        length.append(len(i))
    print(max(length))


# method takes a list of words, return words with length more than 6
def len_6(words1):
    new_list = []
    for i in words1:
        if len(i) >= 6:
            new_list.append(i)
    return new_list


abc = ['fffdff', 'ddsd', '123456']
print(len_6(abc))


# Write a function that will calculate the factorial:
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


print(factorial(6))


# Write a function that will return the count of str object whose length is more than 2 in a list or tuple
def string_counter(abc):
    counter = 0
    for i in abc:
        if isinstance(i, str) and len(i) >= 2:
            counter += 1
    print(counter)


abc = ['fffdff', 'ddsd', '1', 123, None]

string_counter(abc)


# Write a function that removes duplicate from the list
def remove_duplicate(abc):
    single_list = []
    for i in abc:
        if i not in single_list:
            single_list.append(i)
    print(single_list)


abc = ['fffdff', 'ddsd', '1', '1', 123, 123, None]
remove_duplicate(abc)


# another way:

def remove_duplicates(items):
    return list(set(items))


# write is_distinct function to check if a list contains all unique value

def is_distinct(abc):
    if isinstance(abc, set):
        print(True)
    else:
        print(False)


abc = ['fffdff', 'ddsd', '1', '1', 123, 123, None]
is_distinct(abc)


# its given, analyze the result after calling it in three ways

def function(idx, l=[]):
    for i in range(idx):
        l.append(i ** 3)
    print(l)


# function(4)

# function(5, ['a','b','c'])

function(6)

# function given, analyze the results
def function(*args, **kwargs):
    print(args, kwargs)

function(3,4)
function( x = 3, y= 4)
function(1, 2, x = 3, y= 4)

# wrie a function is_paliandrome to determine if they look same from front and back

def is_paliandrome(abc):
    inverse = abc[::-1]
    if inverse == abc:
        return True
    else: return False
print(is_paliandrome('level'))

# transform the given list to a list containing the length of the elements. use map function and lambda
stocks = ['playway', 'boombit', 'cd projekt']
length = list(map(lambda i: len(i), stocks))
print(length)

# Use sort_list to sort two elements tuple according to second element of tuple
def sort_list(items):
    return sorted(items, key=lambda item: item[1])

# make a lambda function for a given function
func_2 = lambda x,y : x+y+2
print(func_2(3,4))

# sort the tuples based on growing sum of squared objects and lambda
items = [(3, 4), (2, 5), (1, 4), (6, 1)]
abc = items.sort(key = lambda i: i[0]**2 + i[1]**2 )
print(items)

# sort the dictionary by price:
stocks = [
    {'indeks': 'mWIG40', 'name': 'TEN', 'price': 304},
    {'indeks': 'mWIG40', 'name': 'PLW', 'price': 309},
    {'indeks': 'sWIG80', 'name': 'BBT', 'price': 22}
]

abc = stocks.sort(key= lambda i : i['price'])
print(stocks)

# filter from the mWIG40 index:

stocks = [
    {'indeks': 'mWIG40', 'name': 'TEN', 'price': 304},
    {'indeks': 'mWIG40', 'name': 'PLW', 'price': 309},
    {'indeks': 'sWIG80', 'name': 'BBT', 'price': 22}
]

print(list(filter(lambda i : i['indeks']== 'mWIG40', stocks)))

# make the dictionary a list of boolean values, True if indeks = 'mWIG40'

stocks = [
    {'indeks': 'mWIG40', 'name': 'TEN', 'price': 304},
    {'indeks': 'mWIG40', 'name': 'PLW', 'price': 309},
    {'indeks': 'sWIG80', 'name': 'BBT', 'price': 22}
]

abc = list(map(lambda i : i['indeks']== 'mWIG40', stocks))
print(abc)

# by using map and lambda, remove the dash (-)

items = ['P-1', 'R-2', 'D-4', 'F-6']
print(list(map(lambda i: i.replace('-', ''), items)))

# make a list with the remainder of first one divided by another:

num1 = [4, 2, 6, 2, 11]
num2 = [5, 2, 3, 3, 9]

print(list(map(lambda x , y: x%y , num1, num2)))

# build a generator which will give only name with .txt extension

fnames = ['abc.txt', 'sds.txt', 'dshdb.jpg']


def file_gen(abc):
    for i in abc:
        if i.endswith('.txt'):
            yield(i)

my_txt = file_gen(fnames)
my_txt_list = []
for txt in my_txt:
    my_txt_list.append(txt)
print(my_txt_list)

#  write a function that acts like enumerate function

def enum(items):
    idx = 0
    for i in items:
        yield(idx, i)
        idx += 1
my_item = enum(my_txt_list)
l = []
for i in my_item:
    l.append(i)
print(l)

# define generator that give today, yesday, tomrw

def dayc(index):
    days = ['mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun']

    yield d_l.append(days[index-1])
    yield d_l.append(days[index])
    yield d_l.append(days[(index+1)%7])
