list1 = []
list2 = []

with open('input.txt', 'r') as file:
    for line in file:
        col1, col2 = map(int, line.split())
        list1.append(col1)
        list2.append(col2)

list1.sort()
list2.sort()

sum = 0
for col1, col2 in zip(list1, list2):
    sum += abs(col1 - col2)

print(f"Sum: {sum}")
