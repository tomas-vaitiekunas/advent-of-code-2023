import copy


def get_data(filename):
    data = []
    with open(filename, 'r') as file:
        line = file.readline().strip()
        while line:
            numbers = [int(s) for s in line.split(' ')]
            data.append(numbers)
            line = file.readline().strip()
    return data


def fill_sequences(s):
    sequences = []
    sequences.append(copy.deepcopy(s))
    i = 0
    all_zeroes = False
    while not all_zeroes:
        new_line = []
        for j in range(1, len(sequences[i])):
            new_line.append(sequences[i][j] - sequences[i][j - 1])
        sequences.append(new_line)
        i += 1
        all_zeroes = True
        for n in new_line:
            if n != 0:
                all_zeroes = False
                break
    return sequences


def run_part1(filename):
    data = get_data(filename)
    total_counter = 0
    for s in data:

        sequences = fill_sequences(s)
        for i in range(len(sequences) - 1, -1, -1):
            if i == len(sequences) - 1:
                sequences[i].append(0)
            else:
                new_number = sequences[i][-1] + sequences[i + 1][-1]
                sequences[i].append(new_number)

        s.append(sequences[0][-1])
        total_counter += s[-1]

    print(f"Total counter : {total_counter}")


def run_part2(filename):
    data = get_data(filename)
    total_counter = 0
    for s in data:

        sequences = fill_sequences(s)
        for i in range(len(sequences) - 1, -1, -1):
            if i == len(sequences) - 1:
                sequences[i].append(0)
            else:
                new_number = sequences[i][0] - sequences[i + 1][0]
                sequences[i].insert(0, new_number)

        s.insert(0, sequences[0][0])
        total_counter += s[0]

    print(f"Total counter : {total_counter}")


if __name__ == "__main__":

    run_part1("input.txt")

# Part1 : 1953784198
# Part2 : 957