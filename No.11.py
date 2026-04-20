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


def read_card_inputs(hand_size):
    card_inputs = []
    for _ in range(hand_size):
        card_inputs.append(input())
    return card_inputs


def parse_hand_cards(card_inputs):
    hand_cards = []
    for card_input in card_inputs:
        mark_str, number_str = card_input.split()
        hand_cards.append((int(mark_str), int(number_str)))
    return hand_cards


def main():
    total_mark_types = int(input())
    total_number_types = int(input())
    hand_size = int(input())

    card_inputs = read_card_inputs(hand_size)
    hand_cards = parse_hand_cards(card_inputs)

    matching_card_count = count_matching_cards(
        total_mark_types,
        total_number_types,
        hand_cards
    )

    print(matching_card_count)


if __name__ == "__main__":
    main()
