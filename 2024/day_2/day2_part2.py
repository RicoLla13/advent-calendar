def check_row(row: list):
    result_diff = check_distance(row)
    if not result_diff:
        row_copy = row.copy()
        rem_duplic(row_copy)
        result_diff = check_distance(row_copy)
        if not result_diff:
            return False

    result_inc = check_incr(row)
    if not result_inc:
        row_copy = row.copy()
        rem_incr(row_copy)
        result_inc = check_incr(row_copy)

    result_dec = check_decr(row)
    if not result_dec:
        row_copy = row.copy()
        rem_decr(row_copy)
        result_dec = check_decr(row_copy)

    return result_inc or result_dec


def rem_duplic(row: list):
    for i in range(1, len(row)):
        diff = abs(row[i - 1] - row[i])
        if diff < 1 or diff > 3:
            row.pop(i)
            break


def rem_incr(row: list):
    for i in range(1, len(row)):
        if row[i - 1] > row[i]:
            row.pop(i - 1)
            break


def rem_decr(row: list):
    for i in range(1, len(row)):
        if row[i - 1] < row[i]:
            del row[i - 1]
            break


def check_distance(row: list):
    for i in range(1, len(row)):
        diff = abs(row[i - 1] - row[i])
        if diff < 1 or diff > 3:
            return False
    return True


def check_incr(row: list):
    for i in range(1, len(row)):
        if row[i - 1] > row[i]:
            return False
    return True


def check_decr(row: list):
    for i in range(1, len(row)):
        if row[i - 1] < row[i]:
            return False
    return True


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
        print(f"Row {i} -> {result}")
        if result:
            safe_reports += 1

    print(f"Total of safe reports: {safe_reports}")
