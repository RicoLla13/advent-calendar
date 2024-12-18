with open("./input.txt", "r") as file:
    two_sum = 0
    three_sum = 0

    for line in file:
        dict_let = {}
        for letter in line:
            if letter not in dict_let.keys():
                dict_let[letter] = 1
            else:
                dict_let[letter] += 1

        two_add = 0
        three_add = 0

        for value in dict_let.values():
            if value == 2:
                two_add = 1
            elif value == 3:
                three_add = 1

        two_sum += two_add
        three_sum += three_add

    print(f"Two: {two_sum}, Three: {three_sum}")
    print(two_sum * three_sum)
