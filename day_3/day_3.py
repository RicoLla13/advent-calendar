import re


def mul(x, y):
    return x * y


with open('./input.txt', 'r') as file:
    content = file.readlines()
    content = ''.join(content)
    operations = re.findall(r"mul\(\d{1,3},\d{1,3}\)", content)

    res = 0

    for op in operations:
        res += eval(op)

    print(res)
