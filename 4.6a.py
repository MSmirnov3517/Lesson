from sys import argv
from itertools import count

script_name, first_number, last_number= argv
for el in count(int(first_number)):
    if el > int(last_number):
        break
    else:
        print(el)

