def check_row(row: list):
    for i in range(1, len(row)):
        diff = abs(row[i - 1] - row[i])
        if diff < 1 or diff > 3:
            copy_row = row.copy()
            copy_row.pop(i)
            print(copy_row)
            if not check_row(copy_row):
                return False

    result_inc = True
    result_dec = True

    # Check for inc
    for i in range(1, len(row)):
        if row[i - 1] > row[i]:
            result_inc = False

    # Check for dec
    for i in range(1, len(row)):
        if row[i - 1] < row[i]:
            result_dec = False

    return result_inc or result_dec


if __name__ == '__main__':
    matrix = []

    with open('input.txt', 'r') as file:
        for line in file:
            row = []
            for x in line.split():
                row.append(int(x))

            matrix.append(row)

    safe_reports = 0
    for i in range(len(matrix)):
        result = check_row(matrix[i])
        print(f"Row {i} -> {check_row(matrix[i])}")
        if result:
            safe_reports += 1

    print(f"Total of safe reports: {safe_reports}")
