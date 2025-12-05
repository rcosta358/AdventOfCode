with open("puzzle_input.txt") as f:
    ranges, ids = f.read().split("\n\n")

res = 0
for i in ids.splitlines():
    id = int(i)
    for r in ranges.splitlines():
        start, end = map(int, r.split("-"))
        if start <= id <= end: # in range?
            res += 1
            break

print(res) # 896