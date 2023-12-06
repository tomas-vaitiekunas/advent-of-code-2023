def get_data(filename):
    data = {}

    with open(filename, 'r') as file:
        line = file.readline()
        while line:
            key = line[:line.index(":")].strip()
            numbers_str = line[line.index(":") + 1:].strip()
            while "  " in numbers_str:
                numbers_str = numbers_str.replace("  ", " ")
            numbers = [int(n) for n in numbers_str.split(" ")]
            data[key] = numbers
            line = file.readline()
    return data


def get_data2(filename):
    data = {}

    with open(filename, 'r') as file:
        line = file.readline()
        while line:
            key = line[:line.index(":")].strip()
            number_str = line[line.index(":") + 1:].strip().replace(" ", "")
            number = int(number_str)
            data[key] = number
            line = file.readline()
    return data


def get_distance(t, limit):
    return t * (limit - t)


def run_part1():
    data = get_data("input.txt")
    win_counts = []
    for i in range(len(data["Time"])):
        win_count = 0
        time = data["Time"][i]
        distance = data["Distance"][i]
        for button_time in range(1, time):
            d = get_distance(button_time, time)
            if d > distance:
                win_count += 1
        win_counts.append(win_count)

    total_count = 1
    for w in win_counts:
        total_count *= w

    print(f"Total count : {total_count}")


def run_part2():
    data = get_data2("input.txt")
    win_count = 0
    for button_time in range(1, data["Time"]):
        d = get_distance(button_time, data["Time"])
        if d > data["Distance"]:
            win_count += 1

    print(f"Total count : {win_count}")


if __name__ == "__main__":

    run_part2()
