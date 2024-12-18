def find_pair(arr):
    for x in arr:
        other = 2020 - x
        if other in arr:
            return x, other
    return -1, -1


if __name__ == "__main__":
    input = []

    with open("./input.txt", "r") as file:
        for line in file:
            input.append(int(line))
        n1, n2 = find_pair(input)
        print(n1 * n2)
