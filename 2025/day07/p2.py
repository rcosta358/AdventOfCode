from collections import defaultdict

with open("puzzle_input.txt") as f:
    lines = f.read().splitlines()

start = lines[0].index('S')
timelines = defaultdict(int) # x -> number of timelines at x
timelines[start] = 1
res = 0

for y in range(len(lines)):
    y_timelines = defaultdict(int)
    for x, count in timelines.items():
        if x < 0 or x >= len(lines[0]): # out of bounds 
            res += count
            break

        val = lines[y][x]
        if val == '^':
            y_timelines[x - 1] += count
            y_timelines[x + 1] += count
        else:
            y_timelines[x] += count
    timelines = y_timelines

res += sum(timelines.values())
print(res) # 15118009521693
