maps = [[], [], [], [], [], [], []]


def find_next(source, current_index):
    global maps
    curr_maps = maps[current_index]
    destination = None
    for map in curr_maps:
        destination_range_start = map[0]
        source_range_start = map[1]
        range_length = map[2]
        if source_range_start <= source <= source_range_start + range_length:
            diff = source - source_range_start
            destination = destination_range_start + diff
            break
    if not destination:
        destination = source
    if current_index == 6:
        return destination
    else:
        return find_next(destination, current_index + 1)


def run_part1():
    global maps
    seeds = []
    locations = []
    map_index = {"seed-to-soil map": 0,
                 "soil-to-fertilizer map": 1,
                 "fertilizer-to-water map": 2,
                 "water-to-light map": 3,
                 "light-to-temperature map": 4,
                 "temperature-to-humidity map": 5,
                 "humidity-to-location map": 6}

    current_index = 0
    with open("input.txt", 'r') as file:
        line = file.readline()
        while line:
            if line.startswith("seeds:"):
                seeds_str = line[line.index(":") + 1:].strip()
                seeds = [int(n) for n in seeds_str.split(" ")]
            elif ":" in line:
                map_key = line[:line.index(":")]
                current_index = map_index[map_key]
            elif line != "\n":
                numbers = [int(n) for n in line.strip().split(" ")]
                maps[current_index].append(numbers)

            line = file.readline()

    for seed in seeds:
        current_index = 0
        location = find_next(seed, current_index)
        locations.append(location)

    print(f"Lowest location number: {min(locations)}")


def run_part2():
    global maps
    map_index = {"seed-to-soil map": 0,
                 "soil-to-fertilizer map": 1,
                 "fertilizer-to-water map": 2,
                 "water-to-light map": 3,
                 "light-to-temperature map": 4,
                 "temperature-to-humidity map": 5,
                 "humidity-to-location map": 6}

    current_index = 0
    with open("input.txt", 'r') as file:
        line = file.readline()
        while line:
            if line.startswith("seeds:"):
                seeds_str = line[line.index(":") + 1:].strip()
                seeds_ranges = [int(n) for n in seeds_str.split(" ")]
            elif ":" in line:
                map_key = line[:line.index(":")]
                current_index = map_index[map_key]
            elif line != "\n":
                numbers = [int(n) for n in line.strip().split(" ")]
                maps[current_index].append(numbers)

            line = file.readline()

    min_location = find_next(seeds_ranges[0], 0)
    step = 10000
    for i in range(1, len(seeds_ranges), 2):
        print(f"Progress {i} / {len(seeds_ranges)}")
        seed_range_start = seeds_ranges[i - 1]
        seed_range_length = seeds_ranges[i]
        seed = seed_range_start
        seed_range_end = seed_range_start + seed_range_length
        while seed < seed_range_end:
            location = find_next(seed, 0)
            if seed + step < seed_range_end:
                location2 = find_next(seed + step, 0)
            else:
                location2 = find_next(seed_range_end - 1, 0)

            if location < min_location:
                min_location = location

            if seed + step < seed_range_end and location2 == location + step:
                seed += step
            else:
                seed += 1

    print(f"Lowest location number: {min_location}")


if __name__ == "__main__":

    run_part2()
