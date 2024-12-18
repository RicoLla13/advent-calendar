list1 = []
list2 = []

with open('input.txt', 'r') as file:
    for line in file:
        col1, col2 = map(int, line.split())
        list1.append(col1)
        list2.append(col2)

sum = 0
for x in list1:
    sum += x * list2.count(x)

print(f"Sum: {sum}")
