with open("puzzle_input.txt") as f:
    lines = f.read().splitlines()

dial = 50
res = 0
for line in lines:
    dir = 1 if line[0] == "R" else -1
    val = int(line[1:]) * dir
    dial = (dial + val) % 100
    if dial == 0:
        res += 1

print(res) # 1123

