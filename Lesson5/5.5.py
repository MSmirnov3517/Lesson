with open('For5.5.txt', 'a') as f:
    f.write('1 10 15 20 25')
summa = 0
with open('For5.5.txt', 'r') as f:
    for el in f.readline().split():
        el = int(el)
        summa += el
print(summa)