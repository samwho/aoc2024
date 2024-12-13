from collections import defaultdict


def delta(a, b):
    return (b[0] - a[0], b[1] - a[1])

def is_point_in_grid(grid, point):
    return 0 <= point[0] < len(grid) and 0 <= point[1] < len(grid[0])

def draw_antinodes(grid, antinodes):
    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            if (y, x) in antinodes:
                print("#", end="")
            else:
                print(cell, end="")
        print()

matching_nodes = defaultdict(list)

with open("day8.data") as f:
    grid = list(map(list, map(str.strip, f.readlines())))

    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            if cell == ".":
                continue
            matching_nodes[cell].append((y, x))

    total = 0
    antinodes = set()
    for key, locations in matching_nodes.items():
        for location in locations:
            for other_location in locations:
                if location == other_location:
                    continue

                dy, dx = delta(location, other_location)
                antinode = (location[0] - dy, location[1] - dx)

                if is_point_in_grid(grid, antinode):
                    antinodes.add(antinode)

    # draw_antinodes(grid, antinodes)
    print(len(antinodes))
