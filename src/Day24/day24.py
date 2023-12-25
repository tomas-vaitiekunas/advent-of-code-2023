def get_data(filename):
    data = []
    with open(filename, 'r') as file:
        line = file.readline().strip()
        while line:
            coordinates_str = line[:line.index("@")]
            coordinates = coordinates_str.split(",")
            x = int(coordinates[0].strip())
            y = int(coordinates[1].strip())
            z = int(coordinates[2].strip())
            speeds_str = line[line.index("@") + 1:]
            speeds = speeds_str.split(",")
            vx = int(speeds[0].strip())
            vy = int(speeds[1].strip())
            vz = int(speeds[2].strip())
            stone = {"x": x, "y": y, "z": z, "vx": vx, "vy": vy, "vz": vz}
            data.append(stone)
            line = file.readline().strip()
    return data


def line(p1, p2):
    a = (p1[1] - p2[1])
    b = (p2[0] - p1[0])
    c = (p1[0]*p2[1] - p2[0]*p1[1])
    return a, b, -c


def intersection(l1, l2):
    D = l1[0] * l2[1] - l1[1] * l2[0]
    Dx = l1[2] * l2[1] - l1[1] * l2[2]
    Dy = l1[0] * l2[2] - l1[2] * l2[0]
    if D != 0:
        x = Dx / D
        y = Dy / D
        return x, y
    else:
        return False


def run_part1(filename):
    data = get_data(filename)
    low = 200000000000000
    high = 400000000000000
    total_count = 0
    for i in range(len(data)):
        for j in range(i + 1, len(data)):
            p1 = (data[i]["x"], data[i]["y"])
            p2 = (data[i]["x"] + data[i]["vx"], data[i]["y"] + data[i]["vy"])
            line1 = line(p1, p2)

            p3 = (data[j]["x"], data[j]["y"])
            p4 = (data[j]["x"] + data[j]["vx"], data[j]["y"] + data[j]["vy"])
            line2 = line(p3, p4)
            X = intersection(line1, line2)
            if X and low <= X[0] <= high and low <= X[1] <= high:
                if (data[i]["vx"] < 0 and X[0] < data[i]["x"] or data[i]["vx"] > 0 and X[0] > data[i]["x"]) and (data[i]["vy"] < 0 and X[1] < data[i]["y"] or data[i]["vy"] > 0 and X[1] > data[i]["y"]):
                    line1_future = True
                else:
                    line1_future = False
                if (data[j]["vx"] < 0 and X[0] < data[j]["x"] or data[j]["vx"] > 0 and X[0] > data[j]["x"]) and (data[j]["vy"] < 0 and X[1] < data[j]["y"] or data[j]["vy"] > 0 and X[1] > data[j]["y"]):
                    line2_future = True
                else:
                    line2_future = False
                if line1_future and line2_future:
                    total_count += 1

    print(f"Total count : {total_count}")


def run_part2(filename):
    data = get_data(filename)
    print("End Part 2")


if __name__ == "__main__":

    run_part1("input.txt")


