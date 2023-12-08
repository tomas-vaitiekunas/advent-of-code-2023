import math


def get_data(filename):
    data = {}
    with open(filename, 'r') as file:
        line = file.readline()
        while line:
            if line == "\n":
                pass
            elif "=" not in line:
                moves = line.strip()
            elif "=" in line:
                pos = line[:line.index("=")].strip()
                left = line[line.index("(") + 1: line.index(",")].strip()
                right = line[line.index(",") + 1: line.index(")")].strip()
                data[pos] = {"L": left, "R": right}
            line = file.readline()
    return moves, data


def run_part1(filename):
    moves, data = get_data(filename)
    i = 0
    moves_count = 0
    pos = "AAA"
    while i < len(moves):
        pos = data[pos][moves[i]]
        moves_count += 1
        if pos[2] == "Z":
            break
        if i == len(moves) - 1:
            i = 0
        else:
            i += 1

    print(f"Moves : {moves_count}")


def run_part2(filename):
    moves, data = get_data(filename)
    positions = []
    for pos in data.keys():
        if pos[2] == "A":
            positions.append(pos)
    p = len(positions)

    z_counts = []
    steps = []
    for i in range(p):
        z_counts.append([])
        steps.append([])

    i = 0
    m = len(moves)
    moves_count = 0
    while i < len(moves):
        for j in range(p):
            positions[j] = data[positions[j]][moves[i]]
        moves_count += 1

        # register move_counts at which each position arrives at 'Z'
        for j in range(p):
            if positions[j][2] == 'Z':
                z_counts[j].append(moves_count)

        finish = True
        # if for all positions we have no less than 3 'Z' arrivals - exit loop
        for j in range(p):
            if len(z_counts[j]) < 3:
                finish = False

        if finish:
            break

        if i == m - 1:
            i = 0
        else:
            i += 1

    # for each position - calculate steps at which this positions arrives at 'Z' and double-check that for each
    # position same step is repeating (obvious, but still ..)
    for i in range(p):
        for j in range(1, len(z_counts[i])):
            steps[i].append(z_counts[i][j] - z_counts[i][j - 1])

    # calculate least common multiple of step numbers from all positions - this will be move number at which all
    # positions will arrive to 'Z'
    result = steps[0][0]
    for i in range(1, p):
        # result = math.gcd(result, steps[i][0])
        result = int((result * steps[i][0]) / math.gcd(result, steps[i][0]))

    print(f"Moves : {result}")
    print(f"Starting points : {len(positions)}")


if __name__ == "__main__":

    run_part2("input.txt")


# Part1 = 19951
# Part2 = 16342438708751
