import re

my_dict = {}
with open('For5.6', 'r', encoding='utf-8') as f:
    while True:
        content = f.readline()
        if not content:
            break
        nums = re.findall('\d+', content)
        nums = [int(i) for i in nums]
        nums = sum(nums)
        key = content[0:content.find(':')]
        other = {key: nums}
        my_dict.update(other)
print(my_dict)