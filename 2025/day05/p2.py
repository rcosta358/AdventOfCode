
with open("puzzle_input.txt") as f:
    ranges, _ = f.read().split("\n\n")

intervals = []
for r in ranges.splitlines():
    start, end = map(int, r.split("-"))
    intervals.append((start, end))

intervals.sort()
merged = [intervals[0]]
for s, e in intervals[1:]:
    ps, pe = merged[-1]
    if s <= pe + 1: # overlap?
        merged[-1] = (ps, max(pe, e)) # merge intervals
    else:
        merged.append((s, e)) # new interval

res = sum(e - s + 1 for s, e in merged)

print(res) # 346240317247002