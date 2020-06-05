age= 20
print("I am %d years old." % (age))
print("My age is: ", age)

lang = 'Python'
ver = '3.8'

print("I'm learning %s version %s" % (lang, ver))
# another way:
print(f"I am learning {lang} version {ver}")

#print Pi up to two digits
pi = 3.1415926535
print(f'Pi: {pi:.2f}')

# prints line of forty dash
print('-'*40)
print("VERSION: 1.0.1")
print('-'*40)

#prints summer#time#holiday
print('summer', 'time', 'holiday', sep = '#')

### math exercise
pi = 3.14
r = 5
Area = pi*(r**2)
print(f"Area: {Area: .1f} in2")

present_value = 1000
interest_rate = 0.03
time = 5
FV = present_value*(1+0.03)**5
print(f"future value is: {FV: .2f} $")

# find the delta of equation: 3x2-4x+1
a = 3
b = -4
c = 1

delta = 4**2-4*3*1
print(f"Delta: {delta: .2f}")

# find sum of first 10 numbers of a = 10+4n
sum=0
for i in range(1 , 11):

    x = 10+4*i
    sum = x + sum
print("sum is:", sum)

## slicing:
#filename = view.jpg, extract only the extension

filename = 'views.jpg'
print(filename[-3:])

string = 'PKV-89415-PLN'
code = (string[0:3]+ string[-3:])
print(code)

string1 = '1 0 1 0 1 3 4 2'
sliced = string1[::2] # takes having a space gap
number = int(sliced)
print(f"the sliced number is: {number: .2f}")

# reverse the string
text = 'Python Course'
print(text[::-1])

# find variable type:
var1 = ''
var2 = ' '
var3 = '\n'

print(type(var1))
print(type(var2))
print((type(var3)))

# isinstance
flag = False
print(isinstance(flag, bool))

# capitalize
text = 'python is a popular programming language. but it is not.'
print(text.capitalize())

# count the number of a letter 'p' in the string
print(f"Number of p in this sentence: {text.count('p')}")

# print true or false depending on whether last four characters of a string matches
code1 = 'FVNISJND-XX-2020'
code2 = 'FVNISJND-XY-2019'

print(f"code1: {code1.endswith('2020')}")
print(f"code2: {code2.endswith('2020')}")

# Check if a string starts with desired text
path1 = 'youtube.com/watch?v=5EhRztVxums'
path2 = 'google.com/search?q=car'

print(f"path1: {path1.startswith('youtube')}")
print(f"path2: {path2.startswith('youtube')}")