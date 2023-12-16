import copy

tiles = []
mirors = []
stable_state_counter = 0
recursion_depth = 100


def get_data(filename):
    data = []
    with open(filename, 'r') as file:
        line = file.readline().strip()
        while line:
            data.append([c for c in line])
            line = file.readline().strip()
    return data


def should_stop(x, y, counter):
    global tiles, recursion_depth
    if tiles[y][x] == '#':
        counter += 1
    if counter >= recursion_depth:
        return True
    return False


def next_tiles(x, y, direction, counter):
    global tiles, mirrors
    counter += 1
    if x == 7 and y == 8:
        pass
    match direction:
        case "right":
            x += 1
            if x == len(tiles[y]):
                # beam leaves to outside
                return None
            else:
                if should_stop(x, y, counter):
                    return None
                tiles[y][x] = '#'
                match mirrors[y][x]:
                    case "-":
                        next_tiles(x, y, "right", counter)
                    case "|":
                        next_tiles(x, y, "up", counter)
                        next_tiles(x, y, "down", counter)
                    case "/":
                        next_tiles(x, y, "up", counter)
                    case "\\":
                        next_tiles(x, y, "down", counter)
                    case '.':
                        next_tiles(x, y, "right", counter)
        case "left":
            x -= 1
            if x == -1:
                # beam leaves to outside
                return None
            else:
                if should_stop(x, y, counter):
                    return None
                tiles[y][x] = '#'
                match mirrors[y][x]:
                    case "-":
                        next_tiles(x, y, "left", counter)
                    case "|":
                        next_tiles(x, y, "up", counter)
                        next_tiles(x, y, "down", counter)
                    case "/":
                        next_tiles(x, y, "down", counter)
                    case "\\":
                        next_tiles(x, y, "up", counter)
                    case '.':
                        next_tiles(x, y, "left", counter)
        case "up":
            y -= 1
            if y == -1:
                # beam leaves to outside
                return None
            else:
                if should_stop(x, y, counter):
                    return None
                tiles[y][x] = '#'
                match mirrors[y][x]:
                    case "-":
                        next_tiles(x, y, "right", counter)
                        next_tiles(x, y, "left", counter)
                    case "|":
                        next_tiles(x, y, "up", counter)
                    case "/":
                        next_tiles(x, y, "right", counter)
                    case "\\":
                        next_tiles(x, y, "left", counter)
                    case '.':
                        next_tiles(x, y, "up", counter)
        case "down":
            y += 1
            if y == len(tiles):
                # beam leaves to outside
                return None
            else:
                if should_stop(x, y, counter):
                    return None
                tiles[y][x] = '#'
                match mirrors[y][x]:
                    case "-":
                        next_tiles(x, y, "right", counter)
                        next_tiles(x, y, "left", counter)
                    case "|":
                        next_tiles(x, y, "down", counter)
                    case "/":
                        next_tiles(x, y, "left", counter)
                    case "\\":
                        next_tiles(x, y, "right", counter)
                    case '.':
                        next_tiles(x, y, "down", counter)
    return None


def run_part1(filename):
    global tiles, mirrors
    mirrors = get_data(filename)
    tiles = copy.deepcopy(mirrors)

    x = -1
    y = 0
    tiles[0][0] = '#'
    direction = "right"
    counter = 0
    next_tiles(x, y, direction, counter)

    for i in range(len(tiles)):
        print(''.join(tiles[i]) + "     " + ''.join(mirrors[i]))

    total_counter = 0
    for i in range(len(tiles)):
        total_counter += tiles[i].count("#")
    print(f"Total number of energized tiles : {total_counter}")


def run_part2(filename):
    global tiles, mirrors, recursion_depth
    recursion_depth = 700
    # recursion_depth = 100
    mirrors = get_data(filename)
    grand_total_counter = 0
    tiles = copy.deepcopy(mirrors)

    for y in range(len(tiles)):
        tiles = copy.deepcopy(mirrors)
        x = -1
        direction = "right"
        counter = 0
        next_tiles(x, y, direction, counter)

        total_counter = 0
        for i in range(len(tiles)):
            total_counter += tiles[i].count("#")
        if total_counter > grand_total_counter:
            grand_total_counter = total_counter

        tiles = copy.deepcopy(mirrors)
        x = len(tiles[y])
        direction = "left"
        counter = 0
        next_tiles(x, y, direction, counter)

        total_counter = 0
        for i in range(len(tiles)):
            total_counter += tiles[i].count("#")
        if total_counter > grand_total_counter:
            grand_total_counter = total_counter

        print(f"Y Progress : {y} / {len(tiles)}")

    for x in range(len(tiles[0])):
        tiles = copy.deepcopy(mirrors)
        y = -1
        direction = "down"
        counter = 0
        next_tiles(x, y, direction, counter)

        total_counter = 0
        for i in range(len(tiles)):
            total_counter += tiles[i].count("#")
        if total_counter > grand_total_counter:
            grand_total_counter = total_counter

        tiles = copy.deepcopy(mirrors)
        y = len(tiles)
        direction = "up"
        counter = 0
        next_tiles(x, y, direction, counter)

        total_counter = 0
        for i in range(len(tiles)):
            total_counter += tiles[i].count("#")
        if total_counter > grand_total_counter:
            grand_total_counter = total_counter

        print(f"X Progress : {x} / {len(tiles[0])}")


    print(f"Grand total number of energized tiles : {grand_total_counter}")


if __name__ == "__main__":

    run_part2("input.txt")


