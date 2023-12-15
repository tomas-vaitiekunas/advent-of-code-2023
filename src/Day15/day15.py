def get_data(filename):
    # data = []
    with open(filename, 'r') as file:
        line = file.readline().strip()
        instructions = line.split(',')
        # while line:
        #     data = instructions
        #     line = file.readline()
    return instructions

def hash_func(instruction):
    current_value = 0
    for c in instruction:
        current_value += ord(c)
        current_value *= 17
        current_value = current_value % 256
    return current_value


def run_part1(filename):
    data = get_data(filename)

    values = []
    for instruction in data:
        current_value = hash_func(instruction)
        values.append(current_value)


    print(f"Total value = {sum(values)}")


def run_part2(filename):
    data = get_data(filename)
    boxes = [{"lenses": [], "focal_lengths": {}} for i in range(256)]
    for instruction in data:
        if '-' in instruction:
            label = instruction[:instruction.index('-')]
            op = '-'
        else:
            label = instruction[:instruction.index('=')]
            op = '='
            focal_length = int(instruction[instruction.index(op) + 1:])

        box_number = hash_func(label)
        if op == '-':
            if label in boxes[box_number]["lenses"]:
                boxes[box_number]["lenses"].remove(label)
        else:
            if label not in boxes[box_number]["lenses"]:
                boxes[box_number]["lenses"].append(label)
            boxes[box_number]["focal_lengths"][label] = focal_length

    focusing_powers = {}
    for i in range(len(boxes)):
        for label in boxes[i]["lenses"]:
            if label in focusing_powers.keys():
                print("???")
                focusing_powers[label] += (i + 1) * (boxes[i]["lenses"].index(label) +1) * boxes[i]["focal_lengths"][label]
            else:
                focusing_powers[label] = (i + 1) * (boxes[i]["lenses"].index(label) + 1) * boxes[i]["focal_lengths"][label]

    total_counter = 0
    for label in focusing_powers.keys():
        total_counter += focusing_powers[label]

    print(f"Total counter : {total_counter}")


if __name__ == "__main__":

    run_part2("input.txt")


