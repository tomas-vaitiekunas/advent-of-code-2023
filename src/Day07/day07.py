cards_sorted = "23456789TJQKA"
cards_sorted_w_jokers = "J23456789TQKA"


def card_rank(card, w_jokers=False):
    global cards_sorted
    global cards_sorted_w_jokers
    if w_jokers:
        return cards_sorted_w_jokers.index(card)
    else:
        return cards_sorted.index(card)


def hand_rank(hand):
    if len(hand) != 5:
        raise Exception("Wrong input detected!")

    unique_cards = len(set(list(hand)))
    if unique_cards == 5:
        # hand has 5 unique cards -> high card 23456
        return 1
    elif unique_cards == 4:
        # one pair 22345
        return 2
    elif unique_cards == 3:
        # two pair 22334 or tree of a kind 22234
        for card in hand:
            if hand.count(card) == 3:
                return 4
        return 3
    elif unique_cards == 2:
        # full-house 22233 or four-of-a-kind 22223
        for card in hand:
            if hand.count(card) == 4:
                return 6
        return 5
    elif unique_cards == 1:
        # five-of-a-kind 22222
        return 7
    else:
        return None

hand_ranks = ["", "high-card", "one-pair", "two-pair", "three", "full-house", "four", "five"]


def upgraded_rank(hand_type, joker_count):
    upgrade_list1 = ["high-card", "one-pair", "three", "four", "five"]
    upgrade_list2 = ["two-pair", "full-house", "four", "five"]
    if hand_type in upgrade_list1:
        index = upgrade_list1.index(hand_type)
        if index + joker_count > len(upgrade_list1) - 1:
            new_hand = "five"
        else:
            new_hand = upgrade_list1[index + joker_count]
    else:
        index = upgrade_list2.index(hand_type)
        if index + joker_count > len(upgrade_list2) - 1:
            new_hand = "five"
        else:
            new_hand = upgrade_list2[index + joker_count]

    new_rank = hand_ranks.index(new_hand)
    return new_rank


def hand_rank_w_jokers(hand):
    if len(hand) != 5:
        raise Exception("Wrong input detected!")
    joker_count = hand.count("J")
    unique_cards = len(set(list(hand)))

    if unique_cards == 5:
        # hand has 5 unique cards -> high card 23456
        r = upgraded_rank("high-card", joker_count)
        return r
    elif unique_cards == 4:
        # one pair 22345
        if joker_count == 1:
            # this hand is upgraded to tree of a kind
            r = upgraded_rank("one-pair", joker_count)
            return r
        elif joker_count == 2:
            return hand_ranks.index("three")
        else:
            return hand_ranks.index("one-pair")
    elif unique_cards == 3:
        # two pair 22334 or tree of a kind 22234
        for card in hand:
            if hand.count(card) == 3:
                if joker_count != 3:
                    r = upgraded_rank("three", joker_count)
                    return r
                else:
                    return hand_ranks.index("four")
        # this is a two pair
        r = upgraded_rank("two-pair", joker_count)
        return r
    elif unique_cards == 2:
        # full-house 22233 or four-of-a-kind 22223
        for card in hand:
            if hand.count(card) == 4:
                if joker_count != 4:
                    # this if four of a kind
                    r = upgraded_rank("four", joker_count)
                    return r
                else:
                    return hand_ranks.index("five")
        r = upgraded_rank("full-house", joker_count)
        return r
    elif unique_cards == 1:
        # five-of-a-kind 22222
        return hand_ranks.index("five")
    else:
        print("ERROR!!")
        return None


def get_data(filename):
    data = []
    with open(filename, 'r') as file:
        line = file.readline()
        while line:
            hand = line[:line.index(" ")]
            bid = int(line[line.index(" ") + 1:].strip())
            data.append({"hand": hand, "bid": bid, "rank": hand_rank(hand)})
            line = file.readline()
    return data


def get_data2(filename):
    data = []
    with open(filename, 'r') as file:
        line = file.readline()
        while line:
            hand = line[:line.index(" ")]
            bid = int(line[line.index(" ") + 1:].strip())
            data.append({"hand": hand, "bid": bid, "rank": hand_rank_w_jokers(hand)})
            line = file.readline()
    return data


def run_part1():
    hands = get_data("input.txt")
    # sort hands according to rank
    changes_made = True
    while changes_made:
        changes_made = False
        for i in range(1, len(hands)):
            if hands[i - 1]["rank"] > hands[i]["rank"]:
                hand_high = hands[i - 1]
                hands[i - 1] = hands[i]
                hands[i] = hand_high
                changes_made = True
                break

    # sort hands with same rank among themselves
    changes_made = True
    while changes_made:
        changes_made = False
        for i in range(1, len(hands)):
            if hands[i - 1]["rank"] == hands[i]["rank"]:
                for j in range(5):
                    if card_rank(hands[i - 1]["hand"][j]) > card_rank(hands[i]["hand"][j]):
                        hand_high = hands[i - 1]
                        hands[i - 1] = hands[i]
                        hands[i] = hand_high
                        changes_made = True
                        break
                    elif card_rank(hands[i - 1]["hand"][j]) == card_rank(hands[i]["hand"][j]):
                        continue
                    else:
                        break
            if changes_made:
                break

    total_count = 0
    for i in range(len(hands)):
        total_count += hands[i]["bid"] * (i + 1)

    print(f"Total count : {total_count}")


def run_part2():
    hands = get_data2("input.txt")
    w_jokers = True
    # sort hands according to rank
    changes_made = True
    while changes_made:
        changes_made = False
        for i in range(1, len(hands)):
            if hands[i - 1]["rank"] > hands[i]["rank"]:
                hand_high = hands[i - 1]
                hands[i - 1] = hands[i]
                hands[i] = hand_high
                changes_made = True
                break

    # sort hands with same rank among themselves
    changes_made = True
    while changes_made:
        changes_made = False
        for i in range(1, len(hands)):
            if hands[i - 1]["rank"] == hands[i]["rank"]:
                for j in range(5):
                    r0 = card_rank(hands[i - 1]["hand"][j], w_jokers)
                    r1 = card_rank(hands[i]["hand"][j], w_jokers)
                    if r0 > r1:
                        hand_high = hands[i - 1]
                        hands[i - 1] = hands[i]
                        hands[i] = hand_high
                        changes_made = True
                        break
                    elif r0 == r1:
                        continue
                    else:
                        break
            if changes_made:
                break

    total_count = 0
    for i in range(len(hands)):
        total_count += hands[i]["bid"] * (i + 1)

    print(f"Total count : {total_count}")


if __name__ == "__main__":

    run_part2()


