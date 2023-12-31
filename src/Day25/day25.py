import copy


def get_data(filename):
    data = []
    with open(filename, 'r') as file:
        line = file.readline().strip()
        while line:
            part = line[:line.index(":")].strip()
            connections = line[line.index(":") + 1:].strip().split(' ')
            data.append({"part": part, "cons": connections})
            line = file.readline()
    return data


def split_cons(connections, i, j, k, pl):
    cons = copy.deepcopy(connections)
    part1 = []
    part2 = []
    c1 = cons[i]
    c2 = cons[j]
    c3 = cons[k]
    cons.remove(c1)
    cons.remove(c2)
    cons.remove(c3)

    loose_parts = list(set([c1[0], c1[1], c2[0], c2[1], c3[0], c3[1]]))
    pl = pl - len(loose_parts)

    part1.append(cons[0][0])
    part1.append(cons[0][1])
    cons.remove(cons[0])

    previous_p = ''
    current_p1_part = part1
    while len(cons) > 0:
        if len(part1) == pl or len(part2) == pl:
            break
        for c in cons:
            p1 = c[0]
            p2 = c[1]

            if p1 == previous_p:
                current_p1_part.append(p2)
                cons.remove(c)
                continue
            else:
                previous_p = p1

            if p1 in part1 and p2 in part2 or p1 in part2 and p2 in part1:
                # merge part2 into part1, wipe part2 and continue
                for j in range(len(part2)):
                    part1.append(part2[j])
                part2 = []
                cons.remove(c)
                current_p1_part = part1
                continue
            elif p1 in part1 and p2 in part1 or p1 in part2 and p2 in part2:
                cons.remove(c)
                continue
            elif p1 in part1 and p2 not in part1:
                part1.append(p2)
                cons.remove(c)
                current_p1_part = part1
                continue
            elif p1 not in part1 and p2 in part1:
                part1.append(p1)
                cons.remove(c)
                current_p1_part = part1
                continue
            elif p1 in part2 and p2 not in part2:
                part2.append(p2)
                cons.remove(c)
                current_p1_part = part2
                continue
            elif p1 not in part2 and p2 in part2:
                part2.append(p1)
                cons.remove(c)
                current_p1_part = part2
                continue
            elif p1 not in part1 and p1 not in part2 and p2 not in part1 and p2 not in part2:
                part2.append(p1)
                part2.append(p2)
                cons.remove(c)
                current_p1_part = part2
                continue
            else:
                continue

    if len(part1) == 0:
        part2 = part2 + loose_parts
    elif len(part2) == 0:
        part1 = part1 + loose_parts
    else:
        for lp in loose_parts:
            if lp not in part1 and lp not in part2:
                print("Problem!")
    part1 = list(set(part1))
    part2 = list(set(part2))

    return len(part1), len(part2), part1, part2


def run_part1(filename):
    data = get_data(filename)
    connections = []
    parts = []
    for part in data:
        parts.append(part["part"])
        for con in part["cons"]:
            connections.append(sorted([part["part"], con]))
            parts.append(con)

    parts = list(set(parts))
    pl = len(parts)
    answer = None
    found_answer = False
    connections = sorted(connections)
    for i in range(len(connections)):
        for j in range(i + 1, len(connections)):
            for k in range(j + 1, len(connections)):
                l_part1, l_part2, part1, part2 = split_cons(connections, i, j, k, pl)
                if l_part1 > 0 and l_part2 > 0:
                    answer = l_part1 * l_part2
                    found_answer = True
                    break
            if found_answer:
                break
        if found_answer:
            break
    print(f"Answer : {answer}")
    print(f"Part1 : {part1}")
    print(f"Part2 : {part2}")


def run_part2(filename):
    data = get_data(filename)
    print("End Part 2")


if __name__ == "__main__":

    run_part1("input.txt")


