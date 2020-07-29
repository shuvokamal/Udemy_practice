# print the calendar using the library:
import calendar
print(calendar.calendar(2020))

# print calendar of July, 2020

print(calendar.month(2020,7))

# Using the datetime library, calculate the differences between two dates:
from datetime import date

date1 = date(2020, 6, 1)
date2 = date(2020, 7, 18)
diff = date2 - date1
print(diff)

# using regular expressions, find out all the digits from the following text

import re
string = 'Python 3.8'
abc = re.findall(pattern="\d", string=string)
print(abc)

# find the alphanumeric from following text:


string = '!@#$%^&45wc'
abc  = re.findall(pattern='\w', string=string)
print(abc)

# using regex, find all the email addresses:

raw_text = "Send an email to info@template.com or sales-info@template.it"
result = re.findall(r"[\w\.-]+@[\w\.-]+", raw_text)
print(result)

# more exercise:
pattern = "[a-zA-Z0-9]+@[a-zA-Z]+\.(com|edu|net)"
user_input = input()
