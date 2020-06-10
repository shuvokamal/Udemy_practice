# find the zero exception:
sum = 3000
counter = 0

try:
    result = sum/counter
    print(result)
except ZeroDivisionError:
    print("Zero division error")

# open a file, show error message if it doesn't exist
try:
    with open("file.txt", 'r') as file:
        content = file.read()
except FileNotFoundError:
    print("File doesn't exists")

# find a value in dictionary, if not found add it
users = {'001': 'Mark', '002': 'Monica', '003': 'Jacob'}
user_id = '004'

try:
    print(users[user_id])
except KeyError:
    print(f"Adding value for user ID {user_id}...")
    users[user_id] = "Kuddus"
    print(users)