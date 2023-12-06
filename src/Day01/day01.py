def run():
    total_sum = 0
    numbers = {"one": "1",
               "two": "2",
               "three": "3",
               "four": "4",
               "five": "5",
               "six": "6",
               "seven": "7",
               "eight": "8",
               "nine": "9"}

    with open("input.txt", 'r') as file:
        line = file.readline()

        while line:
            first_digit = None
            last_digit = None
            first_digit_pos = None
            last_digit_pos = None
            l = len(line)
            for i in range(l):
                if not first_digit and line[i].isdigit():
                    first_digit = line[i]
                    first_digit_pos = i
                if not last_digit and line[l - i - 1].isdigit():
                    last_digit = line[l - i - 1]
                    last_digit_pos = l - i - 1
                if first_digit and last_digit:
                    break
            for n in numbers.keys():
                i = line.find(n)
                if i >= 0:
                    if first_digit_pos is None:
                        first_digit = numbers[n]
                        first_digit_pos = i
                    elif i < first_digit_pos:
                        first_digit = numbers[n]
                        first_digit_pos = i
                    j = line.rfind(n)
                    if last_digit_pos is None:
                        last_digit = numbers[n]
                        last_digit_pos = j
                    elif j >= 0 and j > last_digit_pos:
                        last_digit = numbers[n]
                        last_digit_pos = j

            total_sum += int(first_digit + last_digit)
            line = file.readline()

        print(total_sum)


if __name__ == "__main__":

    run()
