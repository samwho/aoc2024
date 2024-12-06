from collections import defaultdict


def read_input(f):
    rules = defaultdict(list)
    updates = []

    reading_rules = True
    for line in f:
        line = line.strip()
        if line == "":
            reading_rules = False
            continue

        if reading_rules:
            left, right = map(int, line.split("|"))
            rules[left].append(right)
        else:
            updates.append(list(map(int, line.split(","))))

    return rules, updates


def is_order_correct(update, rules):
    expected = []
    seen = set()
    correct = True
    for num in update:
        try:
            expected.remove(num)
        except ValueError:
            pass

        for rule in rules[num]:
            if rule in seen:
                correct = False
                break
            if rule in expected:
                expected.append(rule)

        seen.add(num)

    return correct and len(expected) == 0

def correct_order(update: list[int], rules: dict[int, list[int]]) -> list[int]:
    nums = update[:]
    while True:
        did_swap = False
        for i, num in enumerate(nums):
            for rule in rules[num]:
                if rule not in nums:
                    continue
                rule_idx = nums.index(rule)
                if rule_idx < i:
                    nums[i], nums[rule_idx] = nums[rule_idx], nums[i]
                    did_swap = True
                    break
            if did_swap:
                break
        if not did_swap:
            break
    return nums


with open("day5.data") as f:
    rules, updates = read_input(f)

    total = 0
    for update in updates:
        if not is_order_correct(update, rules):
            update = correct_order(update, rules)
            total += update[len(update) // 2]

    print(total)
