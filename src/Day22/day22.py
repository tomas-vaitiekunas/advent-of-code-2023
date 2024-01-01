import copy
def get_data(filename):
    data = []

    with open(filename, 'r') as file:
        line = file.readline().strip()

        while line:
            pos1_str = line[:line.index("~")]
            pos1_list = pos1_str.split(",")
            pos1_list = [int(c) for c in pos1_list]
            pos2_str = line[line.index("~") + 1:]
            pos2_list = pos2_str.split(",")
            pos2_list = [int(c) for c in pos2_list]
            if pos1_list[2] < pos2_list[2]:
                brick = {"low": pos1_list, "high": pos2_list}
            else:
                brick = {"low": pos2_list, "high": pos1_list}
            data.append(brick)
            line = file.readline().strip()

    return data


def supported(brick, data):
    supported_bricks = []
    x1 = brick["low"][0]
    x2 = brick["high"][0]
    x_range = sorted([x1, x2])
    y1 = brick["low"][1]
    y2 = brick["high"][1]
    y_range = sorted([y1, y2])

    for b in data:
        if b == brick:
            continue

        bx1 = b["low"][0]
        bx2 = b["high"][0]
        bx_range = sorted([bx1, bx2])
        by1 = b["low"][1]
        by2 = b["high"][1]
        by_range = sorted([by1, by2])

        if (b["low"][2] == brick["high"][2] + 1
                and (x_range[0] <= bx_range[0] <= x_range[1] or x_range[0] <= bx_range[1] <= x_range[1] or bx_range[0] <= x_range[0] <= bx_range[1] or bx_range[0] <= x_range[1] <= bx_range[1])
                and (y_range[0] <= by_range[0] <= y_range[1] or y_range[0] <= by_range[1] <= y_range[1] or by_range[0] <= y_range[0] <= by_range[1] or by_range[0] <= y_range[1] <= by_range[1])):
            supported_bricks.append(b)

    return supported_bricks


def other_supporting(supported_brick, data, brick):
    supporting_bricks = []
    x1 = supported_brick["low"][0]
    x2 = supported_brick["high"][0]
    x_range = sorted([x1, x2])
    y1 = supported_brick["low"][1]
    y2 = supported_brick["high"][1]
    y_range = sorted([y1, y2])

    for b in data:
        if b == brick or b == supported_brick:
            continue

        bx1 = b["low"][0]
        bx2 = b["high"][0]
        bx_range = sorted([bx1, bx2])
        by1 = b["low"][1]
        by2 = b["high"][1]
        by_range = sorted([by1, by2])

        if (b["high"][2] + 1 == supported_brick["low"][2]
                and (x_range[0] <= bx_range[0] <= x_range[1] or x_range[0] <= bx_range[1] <= x_range[1] or bx_range[0] <= x_range[0] <= bx_range[1] or bx_range[0] <= x_range[1] <= bx_range[1])
                and (y_range[0] <= by_range[0] <= y_range[1] or y_range[0] <= by_range[1] <= y_range[1] or by_range[0] <= y_range[0] <= by_range[1] or by_range[0] <= y_range[1] <= by_range[1])):
            supporting_bricks.append(b)
            break
    return supporting_bricks


def sort_by_z(data):
    was_change = True
    while was_change:
        was_change = False
        for i in range(len(data) - 1):
            if data[i]["low"][2] > data[i + 1]["low"][2]:
                b = data[i]
                data[i] = data[i + 1]
                data[i + 1] = b
                was_change = True
    return data


def there_is_no_brick_right_below(brick, data):
    if brick["low"][2] == 1:
        return False

    x1 = brick["low"][0]
    x2 = brick["high"][0]
    x_range = sorted([x1, x2])
    y1 = brick["low"][1]
    y2 = brick["high"][1]
    y_range = sorted([y1, y2])

    for b in data:
        if b == brick:
            continue
        if b["high"][2] == brick["low"][2] - 1:
            bx1 = b["low"][0]
            bx2 = b["high"][0]
            bx_range = sorted([bx1, bx2])
            by1 = b["low"][1]
            by2 = b["high"][1]
            by_range = sorted([by1, by2])
            if (x_range[0] <= bx_range[0] <= x_range[1] or x_range[0] <= bx_range[1] <= x_range[1] or bx_range[0] <=
                x_range[0] <= bx_range[1] or bx_range[0] <= x_range[1] <= bx_range[1]) and \
                    (y_range[0] <= by_range[0] <= y_range[1] or y_range[0] <= by_range[1] <= y_range[1] or by_range[
                        0] <= y_range[0] <= by_range[1] or by_range[0] <= y_range[1] <= by_range[1]):
                return False
    return True


def fall_bricks(data):
    for i in range(len(data)):
        while there_is_no_brick_right_below(data[i], data):
            data[i]["low"][2] -= 1
            data[i]["high"][2] -= 1
    return data


def fall_bricks2(data):
    count = 0
    for i in range(len(data)):
        if there_is_no_brick_right_below(data[i], data):
            count += 1
        while there_is_no_brick_right_below(data[i], data):
            data[i]["low"][2] -= 1
            data[i]["high"][2] -= 1
    return count


def run_part1(filename):
    data = get_data(filename)
    counter = 0

    data = sort_by_z(data)

    data = fall_bricks(data)

    for brick in data:
        can_be_removed = True
        supported_bricks = supported(brick, data)

        for supported_brick in supported_bricks:
            other_supporting_bricks = other_supporting(supported_brick, data, brick)
            if len(other_supporting_bricks) > 0:
                continue
            else:
                can_be_removed = False
                break
        if can_be_removed:
            counter += 1

    print(f"Brick count : {counter}")


def run_part2(filename):
    data = get_data(filename)
    counter = 0

    data = sort_by_z(data)
    data = fall_bricks(data)

    for i in range(len(data)):
        new_data = copy.deepcopy(data)
        _ = new_data.pop(i)
        n = fall_bricks2(new_data)
        counter += n
        print(f"Progress {i} / {len(data)}")

    print(f"Brick count : {counter}")


if __name__ == "__main__":

    run_part2("input.txt")

# Part 1 : 530
# Part 2 : 93292