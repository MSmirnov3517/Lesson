while True:
    f = open('mi_file.txt', 'a')
    a = input()
    if a == '':
        break
    f.write(a)
    f.closed
