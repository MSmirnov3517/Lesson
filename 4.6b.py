from sys import argv
from itertools import cycle

script_name, my_list, number_of_repetitions = argv
c = 0
for el in cycle(my_list):
    if c > int(number_of_repetitions):
        break
    print(el)
    c += 1