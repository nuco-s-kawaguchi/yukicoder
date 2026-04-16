from collections import deque


def count_set_bits(x):
    return bin(x).count("1")


def generate_next_positions(pos, N):
    step = count_set_bits(pos)
    candidates = (pos + step, pos - step)
    return [nxt for nxt in candidates if 1 <= nxt <= N]


def breadth_first_search(start, goal, get_next_positions, N):
    if start == goal:
        return 1

    visited = [False] * (N + 1)
    queue = deque([(start, 1)])
    visited[start] = True

    while queue:
        pos, dist = queue.popleft()

        for nxt in get_next_positions(pos):
            if visited[nxt]:
                continue

            if nxt == goal:
                return dist + 1

            visited[nxt] = True
            queue.append((nxt, dist + 1))

    return -1


def main():
    N = int(input())

    start = 1
    goal = N

    def get_next_positions(pos):
        return generate_next_positions(pos, N)

    min_steps = breadth_first_search(start, goal, get_next_positions, N)
    print(min_steps)


if __name__ == "__main__":
    main()