from forklifts import *

with open("puzzle_input.txt") as f:
    lines = f.read().splitlines()

res = 0
for y in range(len(lines)):
    for x in range(len(lines[0])):
        if lines[y][x] == "@" and count_adjacent(x, y, lines) < 4:
            res += 1

print(res) # 1516