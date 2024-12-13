def next_free(data, start):
    for i in range(start, len(data)):
        if data[i] == ".":
            return i
    raise ValueError("No free space found")

def checksum(data: list[str]):
    total = 0
    for i, c in enumerate(data):
        if c == ".":
            continue
        total += i * int(c)
    return total

with open("day9.data") as f:
    data = list(map(int, iter(f.read().strip())))
    print(data)

    file_id = 0
    file = True
    exploded = []
    for num in data:
        for _ in range(num):
            if file:
                exploded.append(str(file_id))
            else:
                exploded.append(".")
        if file:
            file_id += 1
        file = not file

    free = next_free(exploded, 0)

    for i in range(len(exploded) - 1, 0, -1):
        if exploded[i] == ".":
            continue
        if i <= free:
            break

        exploded[free] = exploded[i]
        exploded[i] = "."

        free = next_free(exploded, free)

    print(checksum(exploded))
