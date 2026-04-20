def main():
    number_of_plates = int(input())
    deliciousness_values = list(map(int, input().split()))

    max_up_to_previous = 0
    max_up_to_previous_previous = 0

    for deliciousness in deliciousness_values:
        max_up_to_previous_previous, max_up_to_previous = (
            max_up_to_previous,
            max(
                max_up_to_previous,
                max_up_to_previous_previous + deliciousness
            )
        )

    print(max_up_to_previous)


if __name__ == "__main__":
    main()
