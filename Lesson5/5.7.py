import json

profit_list = []
firm_dict = {}

with open('For5.7', 'r', encoding='utf-8') as f:
    while True:
        content = f.readline().split()
        if not content:
            break
        profit = int(content[2]) - int(content[3])
        if profit > 0:
            profit_list.append(profit)
        firm_dict.update({content[0]: profit})
    average_profit = sum(profit_list) / len(profit_list)
    my_list = [firm_dict, {'average profit': average_profit}]

with open("my_file.json", "w") as write_f:
    json.dump(my_list, write_f)