def is_mas(s: str):
    return s == "MAS" or s == "SAM"

def is_xmas(y: int, x: int, grid: list[list[str]]):
   if y < 1 or y >= len(grid) - 1 or x < 1 or x >= len(grid[y]) - 1:
       return False

   diagonal1 = "".join([grid[y-1][x-1], grid[y][x], grid[y+1][x+1]])
   diagonal2 = "".join([grid[y-1][x+1], grid[y][x], grid[y+1][x-1]])

   return is_mas(diagonal1) and is_mas(diagonal2)

with open("day4.data") as f:
    grid: list[list[str]] = list(map(list, map(str.strip, f.readlines())))
    total = 0

    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if is_xmas(y, x, grid):
                total += 1

    print(total)
