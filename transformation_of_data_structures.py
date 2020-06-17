# set problems
# consider two rolled dice, build the sample space, find the probability of getting more than 10
omega = {(i,j) for i in range(1,7) for j in range(1,7)}
sum_get= {i for i in omega if i[0] + i[1] > 10}
print(f"probability is: {len(sum_get)/len(omega): .2f}")

# all lowercase, remove colon, and the periods,then split text in to words. create set of unique words,
# print length of the set in the console

desc = "Playway: Playway is a producer of computer games."
desc = desc.lower().replace('.', '').replace(':', '')
desc = set(desc.split(' '))
print(len(desc))

# another way
desc = "Playway: Playway is a producer of computer games."
word_list = desc.lower().replace(':', '').replace('.', '').split()
word_unique = {word for word in word_list}
print(len(word_unique))

# consider two rolled dice, build the sample space, find the probability of getting sum of square more than 45
omega = {(i,j) for i in range(1,7) for j in range(1,7)}
square_get = {i for i in omega if i[0]**2 + i[1]**2 >= 45}
print(f"The probability is: {len(square_get)/len(omega): .2f}")

# another way

omega = {(x, y) for x in range(1, 7) for y in range(1, 7)}
a = {(x, y) for x, y in omega if x**2 + y**2 >= 45}
prob = round(len(a) / len(omega), 2)
print(f'Probability: {prob}')

# roll a dice three times, check the probability of sum of three being divisible by 7

omega = {(x, y, z) for x in range(1, 7) for y in range(1, 7) for z in range(1, 7)}
a = {i for i in omega if (i[0]+i[1]+i[2])%7 == 0 }
b = {(x,y,z) for x,y,z in omega if (x+y+z)%7==0}
print(f"probability is {len(a)/len(omega): .2f} ")
print(f"probability is {len(b)/len(omega):.2f}")

# three dices, find if the squares of points divisible by 3:

omega = {(x,y,z) for x in range(1,7) for y in range(1,7) for z in range(1,7)}
a= {(x,y,z) for x,y,z in omega if (x**2 + y**2 + z**2)%3==0}
print(f"The probability is: {len(a)/len(omega): .4f}")

# dice rolled three times, find probability of odd number in each roll:
omega = {(x, y, z) for x in range(1, 7) for y in range(1, 7) for z in range(1, 7)}
a = {(x, y, z) for x, y, z in omega if (x%2 != 0 and y%2 !=0 and z%2 !=0)}
prob = round(len(a) / len(omega), 3)
print(f'Probability: {prob}')