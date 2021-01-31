with open('For5.3.txt', 'r', encoding='utf-8') as f:
    count = 0
    pay = 0
    while True:
        content = f.readline().split()
        if not content:
            break
        if int(content[1]) < 20000:
            print(content[0])
        count +=1
        pay += int(content[1])
    print(pay / count)
