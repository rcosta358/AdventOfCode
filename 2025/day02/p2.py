with open("puzzle_input.txt") as f:
    ranges = f.read().split(",")

res = 0
for r in ranges:
    start, end = map(int, r.split("-"))
    for i in range(start, end + 1):
        s = str(i)
        l = len(s)
        for j in range(1, l):
            if l % j == 0 and s[:j] * (l // j) == s:
                res += i
                break

print(res) # 26202168557