def fact(n):
    c = 1
    for i in range(1,n+1):
        c = c * i
        yield c


for el in fact(5):
    print(el)

