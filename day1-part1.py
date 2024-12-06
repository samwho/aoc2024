import re

with open("day1.data") as f:
    left = []
    right = []
    for line in f:
        [x, y] = map(lambda a: int(a), re.split(r"\s+", line.strip()))
        left.append(x)
        right.append(y)

    left.sort()
    right.sort()

    sum = 0
    for (x, y) in zip(left, right):
        sum += abs(x - y)
    print(sum)
