import copy
import sys
longest_path = 0
max_x = 0
max_y = 0
data = []

def get_data(filename):
    global data
    data = []
    with open(filename, 'r') as file:
        line = file.readline().strip()
        while line:
            data.append([c for c in line])
            line = file.readline().strip()
    return data


def find_next(data, x, y, counter, direction):
    global longest_path, max_x, max_y
    if x > max_x or y > max_y or x < 0 or y < 0:
        return
    if data[y][x] == '#' or data[y][x] == 'O':
        return
    if x == max_x - 1 and y == max_y:
        if counter > longest_path:
            longest_path = counter
            print(f"Longest path = {longest_path}")
            return
    if direction == "down" and data[y][x] == "^":
        return
    elif direction == "up" and data[y][x] == "v":
        return
    elif direction == "left" and data[y][x] == ">":
        return
    elif direction == "right" and data[y][x] == "<":
        return

    new_data = copy.deepcopy(data)
    new_data[y][x] = "O"
    find_next(copy.deepcopy(new_data), x, y + 1, counter + 1, "down")
    find_next(copy.deepcopy(new_data), x, y - 1, counter + 1, "up")
    find_next(copy.deepcopy(new_data), x + 1, y, counter + 1, "right")
    find_next(copy.deepcopy(new_data), x - 1, y, counter + 1, "left")
    return


def find_next2(path, x, y, counter):
    global longest_path, max_x, max_y, data
    if x > max_x or y > max_y or x < 0 or y < 0:
        return
    if data[y][x] == '#':
        return
    if (y, x) in path:
        return
    if x == max_x - 1 and y == max_y:
        if counter > longest_path:
            longest_path = counter
            print(f"Longest path = {longest_path}")
            return
        else:
            print(f"Found not longest path = {counter}")

    new_path = set(path)
    new_path.add((y, x))
    if y + 1 <= max_y and data[y + 1][x] != '#' and (y + 1, x) not in new_path:
        find_next2(set(new_path), x, y + 1, counter + 1)
    if y - 1 >= 0 and data[y - 1][x] != '#' and (y - 1, x) not in new_path:
        find_next2(set(new_path), x, y - 1, counter + 1)
    if x + 1 <= max_x and data[y][x + 1] != '#' and (y, x + 1) not in new_path:
        find_next2(set(new_path), x + 1, y, counter + 1)
    if x - 1 >= 0 and data[y][x - 1] != '#' and (y, x - 1) not in new_path:
        find_next2(set(new_path), x - 1, y, counter + 1)
    return


def run_part1(filename):
    global longest_path, max_x, max_y, data
    sys.setrecursionlimit(10000)
    data = get_data(filename)
    x = 1
    y = 0
    max_x = len(data[0]) - 1
    max_y = len(data) - 1
    data[y][x] = 'O'
    counter = 1
    path = [(y, x)]
    find_next(path, x, y + 1, counter)
    print(f"Longest path = {longest_path}")


def run_part2(filename):
    global longest_path, max_x, max_y, data
    sys.setrecursionlimit(10000)
    data = get_data(filename)
    x = 1
    y = 0
    max_x = len(data[0]) - 1
    max_y = len(data) - 1
    path = set()
    c = (y, x)
    path.add(c)

    counter = 1
    find_next2(path, x, y + 1, counter)

    print(f"Longest path = {longest_path}")


if __name__ == "__main__":

    run_part2("input.txt")


