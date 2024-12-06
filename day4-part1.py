def rows(grid):
    for row in grid:
        yield row

def cols(grid):
    for col in range(len(grid[0])):
        yield [row[col] for row in grid]

# [[1, _, _],
#  [_, 2, _],
#  [_, _, 3]]
def diagonal_down(start, grid):
    y, x = start
    while y < len(grid) and x < len(grid[0]):
        yield grid[y][x]
        y += 1
        x += 1

# [[_, _, 3],
#  [_, 2, _],
#  [1, _, _]]
def diagonal_up(start, grid):
    y, x = start
    while y >= 0 and x < len(grid[0]):
        yield grid[y][x]
        y -= 1
        x += 1

def diagonals(grid):
    width = len(grid[0])
    height = len(grid)

    for y in range(height):
        start = (y, 0)
        yield list(diagonal_down(start, grid))
        yield list(diagonal_up(start, grid))

        start = (y, width - 1)
        yield list(diagonal_down(start, grid))
        yield list(diagonal_up(start, grid))

    for x in range(1, width):
        start = (0, x)
        yield list(diagonal_down(start, grid))
        yield list(diagonal_up(start, grid))

        start = (height - 1, x)
        yield list(diagonal_down(start, grid))
        yield list(diagonal_up(start, grid))

def all_lines(grid):
    yield from rows(grid)
    yield from cols(grid)
    yield from diagonals(grid)

def has_xmas(line):
    return "XMAS" in "".join(line)

def count_occurrences(line, word):
    return "".join(line).count(word)

with open("day4.data") as f:
    grid = list(map(list, map(str.strip, f.readlines())))
    total = 0
    for line in all_lines(grid):
        total += count_occurrences(line, "XMAS")
        total += count_occurrences(reversed(line), "XMAS")
    print(total)
