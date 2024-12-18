with open("./input.txt", "r") as file:
    lines = []
    for line in file:
        lines.append(line)

    for line1 in lines:
        for line2 in lines:
            diffs = 0
            for i in range(len(line1)):
                if line1[i] != line2[i]:
                    diffs += 1
            if diffs == 1:
                print(line1)
                print(line2)
