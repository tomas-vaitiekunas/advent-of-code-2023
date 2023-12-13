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
            break
        for i in range(len(block)):
            if block[i][column - distance] != block[i][column + 1 + distance]:
                match = False
                break
    return match


def check_horizontal(block, line):
    match = True
    for distance in range(len(block)):
        if line - distance < 0 or line + 1 + distance > len(block) - 1:
            break
        for j in range(len(block[0])):
            if block[line - distance][j] != block[line + 1 + distance][j]:
                match = False
                break
    return match


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
            initial_solutions.append({"type": "v", "number": j})
            continue

        # horizontal check
        for i in range(len(block) - 1):
            if check_horizontal(block, i):
                count = i + 1
        if count > 0:
            total_counter += count * 100
            initial_solutions.append({"type": "h", "number": i})
            continue
        else:
            print("Problem!!")

    print(f"Total_counter Part 1: {total_counter}")


def run_part2(filename):
    data = get_data(filename)
    total_counter = 0
    global initial_solutions

    for k in range(len(data)):
        block = data[k]
        found_new_line = False
        for y in range(len(block)):
            if found_new_line:
                break
            for x in range(len(block[y])):
                if block[y][x] == '.':
                    block[y][x] = '#'
                else:
                    block[y][x] = '.'

                # vertical check
                count = 0
                for j in range(len(block[0]) - 1):
                    if check_vertical(block, j) and initial_solutions[k] != {"type": "v", "number": j}:
                        count = j + 1
                        break
                if count > 0:
                    found_new_line = True
                    total_counter += count
                    print("Found new horizontal line!")
                    break

                # horizontal check
                for i in range(len(block) - 1):
                    if check_horizontal(block, i) and initial_solutions[k] != {"type": "h", "number": i}:
                        count = i + 1
                        break
                if count > 0:
                    total_counter += count * 100
                    found_new_line = True
                    print("Found new horizontal line!")
                    break
                else:
                    # return the cell back to it original value
                    if block[y][x] == '.':
                        block[y][x] = '#'
                    else:
                        block[y][x] = '.'

    print(f"Total_counter : {total_counter}")


if __name__ == "__main__":
    filename = "test.txt"
    run_part1(filename)
    run_part2(filename)


