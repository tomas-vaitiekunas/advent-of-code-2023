import copy
import math
data = []

# | is a vertical pipe connecting north and south.
# - is a horizontal pipe connecting east and west.
# L is a 90-degree bend connecting north and east.
# J is a 90-degree bend connecting north and west.
# 7 is a 90-degree bend connecting south and west.
# F is a 90-degree bend connecting south and east.
# . is ground; there is no pipe in this tile.
# S is the starting position of the animal; there is a pipe on this tile, but your sketch doesn't show what shape the pipe has."


def get_data(filename):
    global data
    with open(filename, 'r') as file:
        line = file.readline().strip()
        while line:
            line_turns = []
            for c in line:
                line_turns.append(c)
            data.append(line_turns)
            line = file.readline().strip()
    return data


def get_start():
    global data
    for i in range(len(data)):
        for j in range(len(data[i])):
            if data[i][j] == 'S':
                break
        if data[i][j] == 'S':
            break
    return i, j

def find_directions(i, j):
    global data
    directions = []
    # check above
    if i > 0 and (data[i - 1][j] == '|' or data[i - 1][j] == '7' or data[i - 1][j] == 'F'):
        directions.append("up")
    # check below
    if i < len(data) - 1 and (data[i + 1][j] == '|' or data[i + 1][j] == 'J' or data[i + 1][j] == 'L'):
        directions.append("down")
    # check left
    if j > 0 and (data[i][j - 1] == '-' or data[i][j - 1] == 'L' or data[i][j - 1] == 'F'):
        directions.append("left")
    # check right
    if j < len(data[i]) - 1 and (data[i][j + 1] == '-' or data[i][j + 1] == 'J' or data[i][j + 1] == '7'):
        directions.append("right")
    return directions

def turn(previous_direction, next_direction):
    if previous_direction == "down":
        if next_direction == "left":
            return "right"
        elif next_direction == "right":
            return "left"
        else:
            return "no_turn"
    elif previous_direction == "up":
        if next_direction == "left":
            return "left"
        elif next_direction == "right":
            return "right"
        else:
            return "no_turn"
    elif previous_direction == "left":
        if next_direction == "up":
            return "right"
        elif next_direction == "down":
            return "left"
        else:
            return "no_turn"
    elif previous_direction == "right":
        if next_direction == "up":
            return "left"
        elif next_direction == "down":
            return "right"
        else:
            return "no_turn"
    else:
        return "no_turn"

def next_move(direction, i, j):
    if direction == "up":
        next_i = i - 1
        next_j = j
        if data[next_i][next_j] == '|':
            next_direction = "up"
        elif data[next_i][next_j] == '7':
            next_direction = "left"
        elif data[next_i][next_j] == 'F':
            next_direction = "right"
        else:
            next_direction = None
    elif direction == "down":
        next_i = i + 1
        next_j = j
        if data[next_i][next_j] == '|':
            next_direction = "down"
        elif data[next_i][next_j] == 'J':
            next_direction = "left"
        elif data[next_i][next_j] == 'L':
            next_direction = "right"
        else:
            next_direction = None
    elif direction == "left":
        next_i = i
        next_j = j - 1
        if data[next_i][next_j] == '-':
            next_direction = "left"
        elif data[next_i][next_j] == 'L':
            next_direction = "up"
        elif data[next_i][next_j] == 'F':
            next_direction = "down"
        else:
            next_direction = None
    elif direction == "right":
        next_i = i
        next_j = j + 1
        if data[next_i][next_j] == '-':
            next_direction = "right"
        elif data[next_i][next_j] == 'J':
            next_direction = "up"
        elif data[next_i][next_j] == '7':
            next_direction = "down"
        else:
            next_direction = None

    next_turn = turn(direction, next_direction)
    return next_direction, next_i, next_j, next_turn


def mark_right(i, j, path_coordinates, area):
    global data
    j = j + 1
    while (i, j) not in path_coordinates and j < len(data[i]):
        area[i][j] = 'X'
        j += 1
    return area


def mark_right_down(i, j, path_coordinates, area):
    global data
    start_j = j + 1
    start_i = i + 1

    i = start_i
    j = start_j
    while (i, j) not in path_coordinates:
        i += 1
    end_i = i

    i = start_i
    j = start_j
    while (i, j) not in path_coordinates:
        j += 1
    end_j = j

    for i in range(start_i, end_i):
        for j in range(start_j, end_j):
            if (i, j) not in path_coordinates:
                area[i][j] = 'X'

    return area


def mark_up(i, j, path_coordinates, area):
    i = i - 1
    while (i, j) not in path_coordinates and i > 0:
        area[i][j] = 'X'
        i -= 1
    return area


def mark_left(i, j, path_coordinates, area):
    j = j - 1
    while (i, j) not in path_coordinates and j > 0:
        area[i][j] = 'X'
        j -= 1
    return area


def mark_left_up(i, j, path_coordinates, area):
    start_j = j - 1
    start_i = i - 1

    i = start_i
    j = start_j
    while (i, j) not in path_coordinates:
        i -= 1
    end_i = i

    i = start_i
    j = start_j
    while (i, j) not in path_coordinates:
        j -= 1
    end_j = j

    for i in range(start_i, end_i, -1):
        for j in range(start_j, end_j, -1):
            if (i, j) not in path_coordinates:
                area[i][j] = 'X'

    return area


def mark_down(i, j, path_coordinates, area):
    global data
    i = i + 1
    while (i, j) not in path_coordinates and i < len(data):
        area[i][j] = 'X'
        i += 1
    return area


def mark_left_down(i, j, path_coordinates, area):
    global data
    start_i = i + 1
    start_j = j - 1

    i = start_i
    j = start_j
    while (i, j) not in path_coordinates:
        i += 1
    end_i = i

    i = start_i
    j = start_j
    while (i, j) not in path_coordinates:
        j -= 1
    end_j = j

    for i in range(start_i, end_i):
        for j in range(start_j, end_j, -1):
            if (i, j) not in path_coordinates:
                area[i][j] = 'X'

    return area


def mark_right_up(i, j, path_coordinates, area):
    global data
    start_i = i - 1
    start_j = j + 1

    i = start_i
    j = start_j
    while (i, j) not in path_coordinates:
        i -= 1
    end_i = i

    i = start_i
    j = start_j
    while (i, j) not in path_coordinates:
        j += 1
    end_j = j

    for i in range(start_i, end_i, -1):
        for j in range(start_j, end_j):
            if (i, j) not in path_coordinates:
                area[i][j] = 'X'
    return area

# ???
def calculate_area(path_coordinates, path, side):
    global data
    area = copy.deepcopy(data)
    if side == "right":
        for p in path_coordinates:
            direction = path[p][0]
            turn = path[p][1]
            # if turn == "right":
            #     continue
            if p == (5, 10) or p == (5, 14) or p == (3, 11) or p == (6, 11):
                pass
            if direction == "up":
                area = mark_right(p[0], p[1], path_coordinates, area)
                if turn == "left":
                    area = mark_up(p[0], p[1], path_coordinates, area)
                    area = mark_right_up(p[0], p[1], path_coordinates, area)
            elif direction == "down":
                area = mark_left(p[0], p[1], path_coordinates, area)
                if turn == "left":
                    area = mark_down(p[0], p[1], path_coordinates, area)
                    area = mark_left_down(p[0], p[1], path_coordinates, area)
            elif direction == "left":
                area = mark_up(p[0], p[1], path_coordinates, area)
                if turn == "left":
                    area = mark_left(p[0], p[1], path_coordinates, area)
                    area = mark_left_up(p[0], p[1], path_coordinates, area)
            elif direction == "right":
                area = mark_down(p[0], p[1], path_coordinates, area)
                if turn == "left":
                    area = mark_right(p[0], p[1], path_coordinates, area)
                    area = mark_right_down(p[0], p[1], path_coordinates, area)
    else:
        for p in path_coordinates:
            direction = path[p][0]
            turn = path[p][1]
            if turn == "left":
                continue
            if direction == "up":
                area = mark_left(p[0], p[1], path_coordinates, area)
                if turn == "right":
                    area = mark_up(p[0], p[1], path_coordinates, area)
                    area = mark_left_up(p[0], p[1], path_coordinates, area)
            elif direction == "down":
                area = mark_right(p[0], p[1], path_coordinates, area)
                if turn == "right":
                    area = mark_down(p[0], p[1], path_coordinates, area)
                    area = mark_right_down(p[0], p[1], path_coordinates, area)
            elif direction == "left":
                area = mark_down(p[0], p[1], path_coordinates, area)
                if turn == "right":
                    area = mark_left(p[0], p[1], path_coordinates, area)
                    area = mark_left_down(p[0], p[1], path_coordinates, area)
            elif direction == "right":
                area = mark_up(p[0], p[1], path_coordinates, area)
                if turn == "right":
                    area = mark_right(p[0], p[1], path_coordinates, area)
                    area = mark_right_up(p[0], p[1], path_coordinates, area)

    for i in range(len(area)):
        for j in range(len(area[i])):
            if (i, j) in path_coordinates:
                area[i][j] = '*'

    for i in range(len(area)):
        print(''.join(area[i]))

    area_count = 0
    for i in range(len(area)):
        for j in range(len(area[i])):
            if area[i][j] == "X":
                area_count += 1

    return area_count


def run_part1(filename):
    global data
    data = get_data(filename)
    start_i, start_j = get_start()
    start_directions = find_directions(start_i, start_j)
    direction = start_directions[0]
    path = [(start_i, start_j)]
    path_length = 0
    direction, i, j = next_move(direction, start_i, start_j)
    while (i, j) != (start_i, start_j):
        path.append((i, j))
        path_length += 1
        direction, i, j = next_move(direction, i, j)
    print(f"Path length = {math.ceil(path_length / 2)}")


def run_part2(filename):
    global data
    data = get_data(filename)
    start_i, start_j = get_start()
    start_directions = find_directions(start_i, start_j)
    direction = start_directions[0]
    path_coordinates = [(start_i, start_j)]
    path = {(start_i, start_j): (direction, None)}
    path_length = 0
    direction, i, j, turn = next_move(direction, start_i, start_j)
    turns = {"left": 0, "right": 0, "no_turn": 0}
    while (i, j) != (start_i, start_j):
        path[(i, j)] = (direction, turn)
        path_coordinates.append((i, j))
        direction, i, j, turn = next_move(direction, i, j)
        turns[turn] += 1
        path_length += 1

    if turns["right"] > turns["left"]:
        area = calculate_area(path_coordinates, path, "right")
    elif turns["right"] < turns["left"]:
        area = calculate_area(path_coordinates, path, "left")
    else:
        print("ERROR!!")


    print(f"Area = {area}")


if __name__ == "__main__":

    run_part2("input.txt")


# Part 1 :  6838
# Part 2 : 441 - too low
# Part 2 : 450 - too low
# Part 2 : 451
