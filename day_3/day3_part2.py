import re


def mul(x, y):
    return x * y


with open('./input.txt', 'r') as file:
    content = file.readlines()
    content = ''.join(content)
    operations = re.findall(
            r"(?:mul\(\d{1,3},\d{1,3}\))|(?:do(?:n't)?\(\))",
            content)

    res = 0
    do_op = True

    for op in operations:
        if 'do()' in op:
            do_op = True
        elif "don't()" in op:
            do_op = False
        elif do_op:
            res += eval(op)

    print(res)
