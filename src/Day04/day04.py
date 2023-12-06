def run_part1():
    cards = []

    with open("input.txt", 'r') as file:
        line = file.readline()
        while line:
            winning_numbers_str = line[line.index(":") + 1: line.index("|")]
            winning_numbers = winning_numbers_str.strip().split(" ")
            numbers_str = line[line.index("|") + 1:].replace("  ", " ")
            numbers = numbers_str.strip().split(" ")
            cards.append({"winning_numbers": winning_numbers, "numbers": numbers})
            line = file.readline()

    total_score = 0
    for card in cards:
        card_score = 0
        for number in card["numbers"]:
            if number in card["winning_numbers"]:
                if card_score:
                    card_score *= 2
                else:
                    card_score = 1
        total_score += card_score

    print(f"Total score of all cards : {total_score}")


def run_part2():
    cards = []
    card_counts = {}
    with open("input.txt", 'r') as file:
        line = file.readline()
        while line:
            card_no_str = line[line.index(" "): line.index(":")].strip()
            card_no = int(card_no_str)
            winning_numbers_str = line[line.index(":") + 1: line.index("|")]
            winning_numbers = winning_numbers_str.strip().split(" ")
            numbers_str = line[line.index("|") + 1:].replace("  ", " ")
            numbers = numbers_str.strip().split(" ")
            cards.append({"no": card_no, "count": 1, "winning_numbers": winning_numbers, "numbers": numbers})
            card_counts[card_no] = 1
            line = file.readline()

    total_score = 0
    for card in cards:
        card_score = 0
        for number in card["numbers"]:
            if number in card["winning_numbers"]:
                card_score += 1

        if card_score:
            multiplicator = card_counts[card["no"]]
            for no in range(1, card_score + 1):
                card_counts[card["no"] + no] += 1 * multiplicator

    for key in card_counts:
        total_score += card_counts[key]

    print(f"Total score of all cards : {total_score}")


if __name__ == "__main__":

    run_part2()
