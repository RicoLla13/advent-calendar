def find_res(arr):
    for i in arr:
        for j in arr:
            temp = 2020 - i - j
            if temp in arr:
                print(i * j * temp)


if __name__ == "__main__":
    input = []

    with open("./input.txt", "r") as file:
        for line in file:
            input.append(int(line))

        find_res(input)
