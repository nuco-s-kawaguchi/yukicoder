def main():
    input()
    deliciousness_values = list(map(int, input().split()))

    take_previous = 0
    skip_previous = 0

    for deliciousness in deliciousness_values:
        new_take = skip_previous + deliciousness
        new_skip = max(skip_previous, take_previous)

        take_previous = new_take
        skip_previous = new_skip

    print(max(take_previous, skip_previous))


if __name__ == "__main__":
    main()
