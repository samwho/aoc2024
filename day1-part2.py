import re
from collections import Counter

with open("day1.data") as f:
    left: list[int] = []
    right: list[int]= []
    for line in f:
        [x, y] = map(lambda a: int(a), re.split(r"\s+", line.strip()))
        left.append(x)
        right.append(y)

    right_counts = Counter(right)

    sum = 0
    for x in left:
        sum += x * (right_counts[x] or 0)
    print(sum)
