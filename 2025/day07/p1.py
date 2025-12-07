with open("puzzle_input.txt") as f:
    lines = f.read().splitlines()

start = lines[0].index('S')
points = { start }
res = 0
for y in range(len(lines)):
    for x in range(len(lines[0])):
        val = lines[y][x]
        if val == '^' and x in points:
            points.remove(x)
            points.add(x - 1)
            points.add(x + 1)
            res += 1

print(res) # 1570
