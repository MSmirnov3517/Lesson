with open('For5.2.txt', 'r') as f:
    count = 0
    while True:
        content = f.readline().split()
        if not content:
            break
        print(f'В строке {count +1} - {len(content)} слов')
        count += 1
    print(f'В этом файле - {count} строк')