
from sys import argv

script_name, hours, rate_per_hour, premium = argv
pay = int(hours) * int(rate_per_hour) + int(premium)

print("Зарплата работника : ", pay)
