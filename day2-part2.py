def clamp(n, smallest, largest):
    return max(smallest, min(n, largest))

def with_1_removed(nums):
    for remove in range(len(nums)):
        yield nums[:remove] + nums[remove + 1:]

def is_safe(nums):
    direction = clamp(nums[0] - nums[1], -1, 1)
    for (i, j) in zip(nums, nums[1:]):
        if i == j or abs(i - j) > 3:
            return False

        new_direction = clamp(i - j, -1, 1)
        if new_direction != direction:
            return False

    return True

with open("day2.data") as f:
    total = 0
    for line in f:
        nums = list(map(int, line.strip().split(" ")))

        for sublist in with_1_removed(nums):
            if is_safe(sublist):
                total += 1
                break

    print(total)
