import re

input = open("day3.data", "r").read()

total = 0
enabled = True
for match in re.findall(r"(?:mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\))", input):
    if match == "do()":
        enabled = True
        continue
    if match == "don't()":
        enabled = False
        continue

    if enabled:
        left, right = map(int, match[4:-1].split(","))
        total += left * right
print(total)
