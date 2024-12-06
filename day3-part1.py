import re

input = open("day3.data", "r").read()

total = 0
for match in re.findall(r"mul\(\d{1,3},\d{1,3}\)", input):
    left, right = map(int, match[4:-1].split(","))
    total += left * right
print(total)
