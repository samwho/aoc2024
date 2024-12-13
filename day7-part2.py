from itertools import product

with open("day7.data") as f:
    total = 0
    for line in f:
        target, nums = line.strip().split(":")
        nums = list(map(int, nums.strip().split(" ")))
        target = int(target)


        for operators in product(["+", "*", "||"], repeat=len(nums) - 1):
            result = nums[0]
            for i, operator in enumerate(operators):
                if operator == "+":
                    result += nums[i + 1]
                elif operator == "*":
                    result *= nums[i + 1]
                elif operator == "||":
                    result = int(f"{result}{nums[i + 1]}")

            if result == target:
                total += target
                break

    print(total)
