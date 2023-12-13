import copy
initial_solutions = []

def get_data(filename):
    data = []
    block = []
    with open(filename, 'r') as file:
        line = file.readline()
        while line:
            if line != "\n":
                block.append([c for c in line.strip()])
            else:
                data.append(block)
                block = []
            line = file.readline()
    if block:
        data.append(block)

    return data


def check_vertical(block, column):
    match = True
    for distance in range(len(block[0])):
        if column - distance < 0 or column + 1 + distance > len(block[0]) - 1:
            # # TODO: !!!
            # match = False
            break
        for i in range(len(block)):
            if block[i][column - distance] != block[i][column + 1 + distance]:
                match = False
                break
    return match


def check_vertical2(block, x, k):
    global initial_solutions
    count = 0
    for j in range(len(block[0]) - 1):
        if (check_vertical(block, j)
                and initial_solutions[k] != {"type": "v", "col": j}
                and j - len(block[0]) + j + 1 < x):
            count = j + 1
            break
    return count


def check_horizontal(block, line):
    match = True
    for distance in range(len(block)):
        if line - distance < 0 or line + 1 + distance > len(block) - 1:
            # # TODO: !!!
            # match = False
            break
        for j in range(len(block[0])):
            if block[line - distance][j] != block[line + 1 + distance][j]:
                match = False
                break
    return match


def check_horizontal2(block, y, k):
    global initial_solutions
    count = 0
    for i in range(len(block) - 1):
        if (check_horizontal(block, i)
                and initial_solutions[k] != {"type": "h", "row": i}
                and i - len(block) + i + 1 < y):
            count = i + 1
            break
    return count


def run_part1(filename):
    data = get_data(filename)
    total_counter = 0
    global initial_solutions
    for block in data:
        # vertical check
        count = 0
        for j in range(len(block[0]) - 1):
            if check_vertical(block, j):
                count = j + 1
                break
        if count > 0:
            total_counter += count
            initial_solutions.append({"type": "v", "col": count - 1})
            continue

        # horizontal check
        for i in range(len(block) - 1):
            if check_horizontal(block, i):
                count = i + 1
        if count > 0:
            total_counter += count * 100
            initial_solutions.append({"type": "h", "row": count - 1})
            continue
        else:
            print("Problem!!")

    print(f"Total_counter Part 1: {total_counter}")


def change_cell(block, y, x):
    if block[y][x] == '.':
        block[y][x] = '#'
    else:
        block[y][x] = '.'
    return block


def run_part2(filename):
    data = get_data(filename)
    total_counter = 0
    count_forward = 0
    count_back = 0
    global initial_solutions

    for k in range(len(data)):
        block = copy.deepcopy(data[k])
        found_new_line = False
        for y in range(len(block)):
            if found_new_line:
                break
            for x in range(len(block[y])):
                if x == 5 and y == 15:
                    pass
                block = change_cell(block, y, x)

                # vertical check
                count = check_vertical2(block, x, k)
                if count > 0:
                    found_new_line = True
                    total_counter += count
                    initial_solutions[k]["part2"] = count
                    print("Found new horizontal line!")
                    break

                # horizontal check
                count = check_horizontal2(block, y, k)
                if count > 0:
                    total_counter += count * 100
                    found_new_line = True
                    initial_solutions[k]["part2"] = count
                    print("Found new horizontal line!")
                    break

                # return the cell back to it original value
                block = change_cell(block, y, x)

        if not found_new_line:
            if initial_solutions[k]["type"] == "h":
                count = initial_solutions[k]["row"] + 1
                total_counter += count * 100
            else:
                count = initial_solutions[k]["col"] + 1
                total_counter += count

    print(f"Total_counter : {total_counter}")


if __name__ == "__main__":
    filename = "input.txt"
    run_part1(filename)
    run_part2(filename)

# Part1 : 33975
# Part2: 23919 -> too low
# Part2: 29083
