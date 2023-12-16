import copy
import time


def get_data(filename):
    data = []
    with open(filename, 'r') as file:
        line = file.readline().strip()
        while line:
            data.append(line)
            line = file.readline().strip()
    return data


def shift_right(s):
    while 'O.' in s:
        s = s.replace('O.', '.O')
    return s


def shift_left(s):
    while '.O' in s:
        s = s.replace('.O', 'O.')
    return s


def tilt_north(data, col_l, row_l):
    # for each column
    for j in range(row_l):
        col = ''.join([data[k][j] for k in range(col_l)])
        col = shift_left(col)
        for k in range(col_l):
            data[k] = data[k][:j] + col[k] + data[k][j + 1:]
    return data


def tilt_south(data, col_l, row_l):
    # for each column
    for j in range(row_l):
        col = ''.join([data[k][j] for k in range(col_l)])
        col = shift_right(col)
        for k in range(col_l):
            data[k] = data[k][:j] + col[k] + data[k][j + 1:]
    return data


def tilt_east(data, col_l, row_l):
    for i in range(col_l):
        data[i] = shift_right(data[i])
    return data


def tilt_west(data, col_l, row_l):
    # for each row
    for i in range(col_l):
        data[i] = shift_left(data[i])
    return data


def calculate_load_north(data):
    l = len(data)
    weight = 0
    for i in range(l):
        weight += (l - i) * data[i].count('O')
    return weight


def run_part1(filename):
    data = get_data(filename)
    row_l = len(data[0])
    col_l = len(data)
    data = tilt_north(data, col_l, row_l)
    load = calculate_load_north(data)
    print(f"Load on north side: {load}")


def run_part2(filename):
    data = get_data(filename)
    data_bank = []
    row_l = len(data[0])
    col_l = len(data)
    start_time = time.time()
    duration = 0
    steps = []
    indexes = []
    first = None
    for i in range(1000000000):
        data = tilt_north(data, col_l, row_l)
        data = tilt_west(data, col_l, row_l)
        data = tilt_south(data, col_l, row_l)
        data = tilt_east(data, col_l, row_l)
        if data in data_bank:
            if not first:
                first = copy.deepcopy(data)
            if data == first:
                steps.append(i)
                indexes.append(data_bank.index(data))
            if len(steps) > 20:
                break
        else:
            data_bank.append(copy.deepcopy(data))

        if i % 1000000 == 0:
            if i != 0:
                duration = int((time.time() - start_time) / i * 1000000)
            print(f"Progress : {int(i / 1000000)} / 1000, duration : {duration}")

    step = steps[1] - steps[0]
    last_n = (1000000000 - steps[0] - 1) % step
    data = copy.deepcopy(first)
    if last_n > 0:
        for i in range(last_n):
            data = tilt_north(data, col_l, row_l)
            data = tilt_west(data, col_l, row_l)
            data = tilt_south(data, col_l, row_l)
            data = tilt_east(data, col_l, row_l)

    load = calculate_load_north(data)
    print(f"Load on north side: {load}")


if __name__ == "__main__":

    run_part2("input.txt")

# Part 1 : 106517
# Part 2 : 97195 -> too high
# Part 2 : 79723
