def count_matching_cards(total_mark_types, total_number_types, hand_cards):
    hand_marks = set()
    hand_numbers = set()

    for mark, number in hand_cards:
        hand_marks.add(mark)
        hand_numbers.add(number)

    mark_match = len(hand_marks) * total_number_types
    number_match = len(hand_numbers) * total_mark_types
    double_count = len(hand_marks) * len(hand_numbers)

    return mark_match + number_match - double_count - len(hand_cards)


def read_hand_cards(hand_size):
    return [tuple(map(int, input().split())) for _ in range(hand_size)]


def main():
    total_mark_types = int(input())
    total_number_types = int(input())
    hand_size = int(input())

    hand_cards = read_hand_cards(hand_size)

    matching_card_count = count_matching_cards(
        total_mark_types,
        total_number_types,
        hand_cards
    )

    print(matching_card_count)


if __name__ == "__main__":
    main()
