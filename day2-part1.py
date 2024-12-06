def clamp(n, smallest, largest):
    return max(smallest, min(n, largest))

with open("day2.data") as f:
    total = 0
    for line in f:
        nums = list(map(int, line.strip().split(" ")))

        direction = clamp(nums[0] - nums[1], -1, 1)
        safe = True
        for (i, j) in zip(nums, nums[1:]):
            if i == j or abs(i - j) > 3:
                safe = False
                break

            new_direction = clamp(i - j, -1, 1)
            if new_direction != direction:
                safe = False
                break

        if safe:
            total += 1

    print(total)
