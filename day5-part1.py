from collections import defaultdict

with open("day5.data") as f:
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

    total = 0
    for update in updates:
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

        if correct and len(expected) == 0:
            total += update[len(update) // 2]

    print(total)
