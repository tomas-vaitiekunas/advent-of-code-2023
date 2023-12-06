import copy

engine = []
used = []
h = 0
l = 0


def get_digits_to_the_right(y, x):
    global engine, used, l
    right = ''
    i = x + 1
    c = engine[y][i]
    while c.isdigit():
        if used[y][i] != ".":
            used[y][i] = "."
            right += c
            i += 1
            if i == l:
                break
            c = engine[y][i]
        else:
            break
    return right


def get_digits_to_the_left(y, x):
    global engine, used
    left = ''
    i = x - 1
    c = engine[y][i]
    while c.isdigit():
        if used[y][i] != ".":
            used[y][i] = "."
            left = c + left
            i -= 1
            if i < 0:
                break
            c = engine[y][i]
        else:
            break
    return left


def get_number(j, i, right_only=False, left_only=False):
    global engine, used
    if used[j][i] == ".":
        return 0
    used[j][i] = "."
    n_str = engine[j][i]
    if not left_only:
        n_str = n_str + get_digits_to_the_right(j, i)
    if not right_only:
        n_str = get_digits_to_the_left(j, i) + n_str
    n = int(n_str)
    return n


def get_numbers_around(y, x):
    sum_local = 0
    global engine, used, h, l

    if y > 0:
        # check above-directly
        if engine[y - 1][x] != "." and engine[y - 1][x].isdigit():
            sum_local += get_number(y - 1, x)

        # check above-left
        if x > 0 and engine[y - 1][x - 1] != "." and engine[y - 1][x - 1].isdigit():
            sum_local += get_number(y - 1, x - 1)

        # check above-right
        if x < l - 1 and engine[y - 1][x + 1] != "." and engine[y - 1][x + 1].isdigit():
            sum_local += get_number(y - 1, x + 1)

    if y < h - 1:
        # check below-directly
        if engine[y + 1][x] != "." and engine[y + 1][x].isdigit():
            sum_local += get_number(y + 1, x)

        # check below-left
        if x > 0 and engine[y + 1][x - 1] != "." and engine[y + 1][x - 1].isdigit():
            sum_local += get_number(y + 1, x - 1)

        # check below-right
        if x < l - 1 and engine[y + 1][x + 1] != "." and engine[y + 1][x + 1].isdigit():
            sum_local += get_number(y + 1, x + 1)

    # check to the left
    if x > 0 and engine[y][x - 1] != "." and engine[y][x - 1].isdigit():
        sum_local += get_number(y, x - 1, left_only=True)

    # check to the right
    if x < l - 1 and engine[y][x + 1] != "." and engine[y][x + 1].isdigit():
        sum_local += get_number(y, x + 1, right_only=True)

    return sum_local


def get_gear_ratio(y, x):
    sum_local = 0
    global engine, used, h, l
    numbers = []

    if y > 0:
        # check above-directly
        if engine[y - 1][x] != "." and engine[y - 1][x].isdigit():
            n = get_number(y - 1, x)
            if n > 0:
                numbers.append(n)

        # check above-left
        if x > 0 and engine[y - 1][x - 1] != "." and engine[y - 1][x - 1].isdigit():
            n =  get_number(y - 1, x - 1)
            if n > 0:
                numbers.append(n)

        # check above-right
        if x < l - 1 and engine[y - 1][x + 1] != "." and engine[y - 1][x + 1].isdigit():
            n = get_number(y - 1, x + 1)
            if n > 0:
                numbers.append(n)

    if y < h - 1:
        # check below-directly
        if engine[y + 1][x] != "." and engine[y + 1][x].isdigit():
            n = get_number(y + 1, x)
            if n > 0:
                numbers.append(n)

        # check below-left
        if x > 0 and engine[y + 1][x - 1] != "." and engine[y + 1][x - 1].isdigit():
            n = get_number(y + 1, x - 1)
            if n > 0:
                numbers.append(n)

        # check below-right
        if x < l - 1 and engine[y + 1][x + 1] != "." and engine[y + 1][x + 1].isdigit():
            n = get_number(y + 1, x + 1)
            if n > 0:
                numbers.append(n)

    # check to the left
    if x > 0 and engine[y][x - 1] != "." and engine[y][x - 1].isdigit():
        n = get_number(y, x - 1, left_only=True)
        if n > 0:
            numbers.append(n)

    # check to the right
    if x < l - 1 and engine[y][x + 1] != "." and engine[y][x + 1].isdigit():
        n = get_number(y, x + 1, right_only=True)
        if n > 0:
            numbers.append(n)

    if len(numbers) == 2:
        return numbers[0] * numbers[1]
    else:
        return 0


def run_part1():

    global engine, used, l, h
    engine = []
    with open("input.txt", 'r') as file:
        line = file.readline()
        while line:
            engine.append([c for c in line.strip()])
            line = file.readline()

    used = copy.deepcopy(engine)
    h = len(engine)
    l = len(engine[0])
    total_sum = 0

    for y in range(h):
        for x in range(l):
            c = engine[y][x]
            if c == ".":
                continue
            elif c.isdigit():
                continue
            else:
                total_sum += get_numbers_around(y, x)

    print(total_sum)


def run_part2():
    global engine, used, l, h
    engine = []
    with open("input.txt", 'r') as file:
        line = file.readline()
        while line:
            engine.append([c for c in line.strip()])
            line = file.readline()

    used = copy.deepcopy(engine)
    h = len(engine)
    l = len(engine[0])
    total_sum = 0

    for y in range(h):
        for x in range(l):
            c = engine[y][x]
            if c == "*":
                total_sum += get_gear_ratio(y, x)

    print(total_sum)


if __name__ == "__main__":

    run_part2()
