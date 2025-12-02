with open("puzzle_input.txt") as f:
    ranges = f.read().split(",")

res = 0
for r in ranges:
    start, end = map(int, r.split("-"))
    for i in range(start, end + 1):
        s = str(i)
        l = len(s)
        if l % 2 == 0 and s[:l//2] == s[l//2:]:
            res += i

print(res) # 18893502033