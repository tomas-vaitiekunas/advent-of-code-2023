def run_part1():
    limits = {"red": 12, "green": 13, "blue": 14}
    total_sum = 0
    with open("input.txt", 'r') as file:
        line = file.readline()

        # Check if the line is not empty
        while line:
            s = line.strip()
            game_id = s[5: s.index(":")]
            s = s[s.index(":") + 1:]
            game_possible = True
            while s:
                i = s.find(";")
                if i > 0:
                    draw = s[:i]
                    s = s[i + 1:]
                else:
                    draw = s
                    s = ''
                cubes = draw.split(",")
                for cube in cubes:
                    j = cube.index(' ', 1)
                    n_str = cube[:j].strip()
                    n = int(n_str)
                    color = cube[j + 1:].strip()
                    if n > limits[color]:
                        game_possible = False
                        break
                if not game_possible:
                    break

            if game_possible:
                total_sum += int(game_id)

            line = file.readline()

        print(total_sum)


def run_part2():
    total_sum = 0
    with open("input.txt", 'r') as file:
        line = file.readline()

        while line:
            s = line.strip()
            s = s[s.index(":") + 1:]
            min_game = {"red": 0, "green": 0, "blue": 0}
            while s:
                i = s.find(";")
                if i > 0:
                    draw = s[:i]
                    s = s[i + 1:]
                else:
                    draw = s
                    s = ''
                cubes = draw.split(",")
                for cube in cubes:
                    j = cube.index(' ', 1)
                    n_str = cube[:j].strip()
                    n = int(n_str)
                    color = cube[j + 1:].strip()
                    if n > min_game[color]:
                        min_game[color] = n

            power = 1
            for color in min_game.keys():
                power *= min_game[color]
            total_sum += power

            line = file.readline()

        print(total_sum)


if __name__ == "__main__":

    run_part2()
