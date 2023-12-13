import copy
from itertools import permutations, combinations, product
def get_data(filename):
    lines = []
    groups = []
    with open(filename, 'r') as file:
        line = file.readline().strip()
        while line:
            positions = line[:line.index(' ')].strip()
            lines.append(positions)
            number_str = line[line.index(' ') + 1:].split(",")
            numbers = [int(c) for c in number_str]
            groups.append(numbers)
            line = file.readline().strip()
    return lines, groups


def check_ok(next_gs, line):
    s = ''.join(next_gs)
    for j in range(len(line)):
        if s[j] == "#" and line[j] == "." or s[j] == "." and line[j] == "#":
            return False
    return True


def make_next(gs, last_gs):
    for i in range(len(gs) - 1, 0, -1):
        if gs[i] == '.' and gs[i - 1] != '.' and (i == len(gs) - 1 or gs[i + 1] == '.'):
            gs[i] = gs[i - 1]
            gs[i - 1] = '.'
            if gs[-1] != "." and i != len(gs) - 1 and gs != last_gs:
                no_more_moves = False
                while not no_more_moves:
                    no_more_moves = True
                    for j in range(i + 2, len(gs) - 1):
                        if gs[j - 1] == '.' and gs[j] == '.' and gs[j + 1] != '.':
                            gs[j] = gs[j + 1]
                            gs[j + 1] = '.'
                            no_more_moves = False
                            break

            return gs
    return None


def make_gs(gn, line):
    gs = []
    l = 0
    for n in gn:
        g_str = ''.join(["#" for j in range(n)])
        gs.append(g_str)
        l += n
        if len(gs) < len(gn) * 2 - 1:
            gs.append(".")
            l += 1
    last_gs = copy.deepcopy(gs)
    while l < len(line):
        gs.append(".")
        last_gs.insert(0, ".")
        l += 1
    return gs, last_gs


def run_part1(filename):
    lines, groups = get_data(filename)
    total_counter = 0
    for i in range(len(lines)):
        line = lines[i]
        gn = groups[i]
        gs, last_gs = make_gs(gn, line)

        p_count = 0
        next_gs = gs
        while next_gs:
            if check_ok(next_gs, line):
                p_count += 1
            next_gs = make_next(next_gs, last_gs)

        total_counter += p_count

    print(f"Total counter : {total_counter}")

def expand_lines(lines):
    expanded_lines = []
    for line in lines:
        expanded_line = (line + '?')*4 + line
        expanded_lines.append(expanded_line)
    return expanded_lines


def expand_groups(groups):
    expanded_groups = []
    for group in groups:
        expanded_group = group * 5
        expanded_groups.append(expanded_group)
    return expanded_groups


def run_part2(filename):
    lines, groups = get_data(filename)
    lines = expand_lines(lines)
    groups = expand_groups(groups)
    total_counter = 0
    for i in range(len(lines)):
        line = lines[i]
        gn = groups[i]
        gs, last_gs = make_gs(gn, line)

        p_count = 0
        next_gs = gs
        while next_gs:
            if check_ok(next_gs, line):
                p_count += 1
            next_gs = make_next(next_gs, last_gs)

        total_counter += p_count

    print(f"Total counter : {total_counter}")
    print("End Part 2")


if __name__ == "__main__":

    run_part2("test.txt")


