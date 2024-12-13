from typing import cast

Entry = tuple[int | None, int]

def color(s: str, color: str) -> str:
    if color == "red":
        return f"\033[91m{s}\033[0m"
    elif color == "green":
        return f"\033[92m{s}\033[0m"
    raise ValueError(f"Unknown color: {color}")

def first_free_of_size(data: list[Entry], size) -> int | None:
    for i, entry in enumerate(data):
        if entry[0] is None and entry[1] >= size:
            return i
    return None

def is_file(entry: Entry) -> bool:
    return entry[0] is not None

def is_free(entry: Entry) -> bool:
    return entry[0] is None

def coalesce(data: list[Entry]) -> list[Entry]:
    new_data: list[Entry] = []
    for entry in data:
        if not new_data:
            new_data.append(entry)
        elif is_free(new_data[-1]) and is_free(entry):
            new_data[-1] = (None, new_data[-1][1] + entry[1])
        else:
            new_data.append(entry)
    return new_data

def swap(data: list[Entry], i1: int, i2: int):
    assert i1 < i2
    assert is_free(data[i1])
    assert is_file(data[i2])

    free = data[i1]
    file = data[i2]

    if free[1] == file[1]:
        data[i1], data[i2] = data[i2], data[i1]
    else:
        data[i1] = (file[0], file[1])
        new_entry = (None, free[1] - file[1])
        data[i2] = (None, file[1])
        data.insert(i1 + 1, new_entry)

def print_data(data: list[Entry], swap: tuple[int, int] | None = None):
    for i, entry in enumerate(data):
        to_print = ""
        if is_free(entry):
            to_print = "." * entry[1]
        else:
            to_print = f"{entry[0]}" * entry[1]

        if swap is not None and i in swap:
            to_print = color(to_print, i == swap[0] and "red" or "green")
        print(f"{to_print}|", end="")
    print()

def find_file_id(data: list[Entry], file_id: int) -> int | None:
    for i, entry in enumerate(data):
        if is_file(entry) and entry[0] == file_id:
            return i
    return None

def checksum(data: list[Entry]):
    total = 0
    i = 0
    for entry in data:
        if is_free(entry):
            i += entry[1]
        elif is_file(entry):
            for _ in range(entry[1]):
                total += i * cast(int, entry[0])
                i += 1
    return total

with open("day9.data") as f:
    data = list(map(int, iter(f.read().strip())))

    file_id = 0
    file = True
    exploded: list[Entry] = []
    for num in data:
        if file:
            exploded.append((file_id, num))
            file_id += 1
        else:
            exploded.append((None, num))
        file = not file


    for id in range(file_id - 1, 0, -1):
        entry_idx = find_file_id(exploded, id)
        assert entry_idx

        entry = exploded[entry_idx]
        free_idx = first_free_of_size(exploded, entry[1])
        if free_idx is None or free_idx >= entry_idx:
            continue

        swap(exploded, free_idx, entry_idx)
        exploded = coalesce(exploded)

    print(checksum(exploded))
