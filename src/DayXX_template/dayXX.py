def get_data(filename):
    data = []
    with open(filename, 'r') as file:
        line = file.readline().strip()
        while line:
            # logic here
            line = file.readline().strip()
    return data


def run_part1(filename):
    data = get_data(filename)
    print("End Part 1")


def run_part2(filename):
    data = get_data(filename)
    print("End Part 2")


if __name__ == "__main__":

    run_part1("test.txt")


