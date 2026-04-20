def count_matching_cards(W, H, hand_cards):
    hand_marks = set()
    hand_numbers = set()

    for mark, number in hand_cards:
        hand_marks.add(mark)
        hand_numbers.add(number)

    mark_match = len(hand_marks) * H
    number_match = len(hand_numbers) * W
    double_count = len(hand_marks) * len(hand_numbers)

    return mark_match + number_match - double_count - len(hand_cards)


def main():
    W = int(input())
    H = int(input())
    N = int(input())

    hand_cards = [tuple(map(int, input().split())) for _ in range(N)]

    result = count_matching_cards(W, H, hand_cards)
    print(result)


if __name__ == "__main__":
    main()
