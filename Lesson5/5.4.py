with open('For5.4.txt', 'r', encoding='utf-8') as f:
    count = 0
    rus_list = ['Один', 'Два', 'Три', 'Четыре']
    while True:
        content = f.readline().split()
        if not content:
            break
        del content[0]
        content.insert(0, rus_list[count])
        count += 1
        new_list = ' '.join(content)
        print(new_list)
        with open("For5.4a.txt", "a", encoding='utf-8') as rus_text:
            print(new_list, file=rus_text)
