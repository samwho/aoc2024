from typing import Literal, Tuple


def is_out_of_bounds(grid: list[list[str]], y: int, x: int) -> bool:
    return y < 0 or y >= len(grid) or x < 0 or x >= len(grid[y])

def rotate_guard(grid: list[list[str]], y: int, x: int):
    if grid[y][x] == "^":
        grid[y][x] = ">"
    elif grid[y][x] == ">":
        grid[y][x] = "v"
    elif grid[y][x] == "v":
        grid[y][x] = "<"
    elif grid[y][x] == "<":
        grid[y][x] = "^"
    else:
        raise ValueError("Not a guard")

def next_pos(y: int, x: int, direction: str) -> Tuple[int, int]:
    if direction == "up":
        return y - 1, x
    elif direction == "down":
        return y + 1, x
    elif direction == "left":
        return y, x - 1
    elif direction == "right":
        return y, x + 1
    else:
        raise ValueError("Invalid direction")

def guard_direction(grid: list[list[str]], y: int, x: int) -> Literal["up", "down", "left", "right"]:
    val = grid[y][x]
    if val == "^":
        return "up"
    elif val == "v":
        return "down"
    elif val == "<":
        return "left"
    elif val == ">":
        return "right"
    else:
        raise ValueError("Not a guard")

def is_guard(grid: list[list[str]], y: int, x: int) -> bool:
    val = grid[y][x]
    return val == "^" or val == "v" or val == "<" or val == ">"

def is_obstacle(grid: list[list[str]], y: int, x: int) -> bool:
    return grid[y][x] == "#"

def find_guard(grid: list[list[str]]) -> Tuple[int, int]:
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if is_guard(grid, y, x):
                return y, x
    raise ValueError("No guard found")

with open("day6.data") as f:
    grid: list[list[str]] = list(map(list, map(str.strip, f.readlines())))

    guard_pos = find_guard(grid)
    visited = set()
    while True:
        visited.add(guard_pos)
        direction = guard_direction(grid, *guard_pos)
        new_pos = next_pos(*guard_pos, direction)
        if is_out_of_bounds(grid, *new_pos):
            break

        if is_obstacle(grid, *new_pos):
            rotate_guard(grid, *guard_pos)
            continue

        grid[new_pos[0]][new_pos[1]] = grid[guard_pos[0]][guard_pos[1]]
        grid[guard_pos[0]][guard_pos[1]] = "."
        guard_pos = new_pos

    print(len(visited))
