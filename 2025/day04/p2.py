from forklifts import *

with open("puzzle_input.txt") as f:
    lines = f.read().splitlines()

res = 0
while True:
    found = False
    for y in range(len(lines)):
        for x in range(len(lines[0])):
            if lines[y][x] == "@" and count_adjacent(x, y, lines) < 4:
                res += 1
                lines[y] = lines[y][:x] + "." + lines[y][x+1:] # replace @ with .
                found = True
    if not found:
        break

print(res) # 9122