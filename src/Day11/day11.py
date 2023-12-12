import copy
from itertools import combinations

def get_data(filename):
    data = []
    with (open(filename, 'r') as file):
        line = file.readline().strip()
        while line:
            points = []
            for c in line:
                points.append(c)
            data.append(points)
            line = file.readline().strip()
    return data

def expand(data):

    new_data = copy.deepcopy(data)
    inserts = 0
    for j in range(len(data[0])):
        empty = True
        for i in range(len(data)):
            if data[i][j] == "#":
                empty = False
                break
        if empty:
            for i in range(len(data)):
                new_data[i].insert(j + inserts, '.')
            inserts += 1

    data = copy.deepcopy(new_data)

    new_data = []
    for i in range(len(data)):
        new_data.append(data[i])
        if '#' not in data[i]:
            new_data.append(data[i])

    data = copy.deepcopy(new_data)

    return data


def expand2(data):

    new_data = copy.deepcopy(data)
    inserts = 0
    for j in range(len(data[0])):
        empty = True
        for i in range(len(data)):
            if data[i][j] == "#":
                empty = False
                break
        if empty:
            for i in range(len(data)):
                new_data[i][j] = 'X'
            inserts += 1

    data = copy.deepcopy(new_data)

    new_data = []
    for i in range(len(data)):
        if '#' not in data[i]:
            new_data.append(['X' for c in data[i]])
        else:
            new_data.append(data[i])
    data = copy.deepcopy(new_data)

    return data

def run_part1(filename):
    data = get_data(filename)
    data = expand(data)
    galaxy_no = 0
    galaxies = {}
    for y in range(len(data)):
        for x in range(len(data[y])):
            if data[y][x] == "#":
                data[y][x] = galaxy_no
                galaxy_no += 1
                galaxies[galaxy_no] = (y, x)

    galaxy_numbers = list(galaxies.keys())
    galaxy_pairs = list(combinations(galaxy_numbers, 2))
    galaxy_pair_distances = {}
    for p in galaxy_pairs:
        g1 = p[0]
        g2 = p[1]
        d = abs(galaxies[g1][0] - galaxies[g2][0]) + abs(galaxies[g1][1] - galaxies[g2][1])
        galaxy_pair_distances[p] = d

    total_sum = 0
    for d in galaxy_pair_distances.keys():
        total_sum += galaxy_pair_distances[d]
    print(f"Total distance : {total_sum}")


def get_distance(data, galaxies, g1, g2):
    multiplicator = 1000000
    y1 = galaxies[g1][0]
    x1 = galaxies[g1][1]
    y2 = galaxies[g2][0]
    x2 = galaxies[g2][1]

    y_mult = 0
    if y2 > y1:
        start = y1
        finish = y2
    else:
        start = y2
        finish = y1
    for i in range(start, finish + 1):
        if data[i][x1] == 'X':
          y_mult += 1

    x_mult = 0
    if x2 > x1:
        start = x1
        finish = x2
    else:
        start = x2
        finish = x1
    for j in range(start, finish + 1):
        if data[y1][j] == 'X':
          x_mult += 1

    d = (abs(galaxies[g1][0] - galaxies[g2][0]) - y_mult + y_mult * multiplicator +
         abs(galaxies[g1][1] - galaxies[g2][1]) - x_mult + x_mult * multiplicator)


    return d


def run_part2(filename):
    data = get_data(filename)
    data = expand2(data)

    galaxy_no = 0
    galaxies = {}
    for y in range(len(data)):
        for x in range(len(data[y])):
            if data[y][x] == "#":
                data[y][x] = str(galaxy_no)
                galaxies[galaxy_no] = (y, x)
                galaxy_no += 1

    # for i in range(len(data)):
    #     print(''.join(data[i]))

    galaxy_numbers = list(galaxies.keys())
    galaxy_pairs = list(combinations(galaxy_numbers, 2))
    galaxy_pair_distances = {}
    for p in galaxy_pairs:
        d = get_distance(data, galaxies, p[0], p[1])
        galaxy_pair_distances[p] = d

    total_sum = 0
    for d in galaxy_pair_distances.keys():
        total_sum += galaxy_pair_distances[d]
    print(f"Total distance : {total_sum}")


if __name__ == "__main__":

    run_part2("input.txt")


