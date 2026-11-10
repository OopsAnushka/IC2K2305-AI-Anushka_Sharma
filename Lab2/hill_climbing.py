
def hill_climbing(start, values):
    current = start

    while True:
        neighbours = [
            current - 1,
            current + 1
        ]

        best = current

        for neighbour in neighbours:
            if neighbour in values and values[neighbour] > values[best]:
                best = neighbour

        if best == current:
            break

        current = best

    return current

values = {
    0: 2,
    1: 5,
    2: 8,
    3: 6,
    4: 10,
    5: 7
}

result = hill_climbing(0, values)

print("Best state:", result)
print("Maximum value:", values[result])
