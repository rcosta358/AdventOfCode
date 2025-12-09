from rect import *

with open("puzzle_input.txt") as f:
    lines = f.read().splitlines()

points = [tuple(map(int, line.split(','))) for line in lines]
max_area = 0
for i in range(len(points)):
    for j in range(i + 1, len(points)):
        area = rect_area(points[i], points[j])
        if area > max_area:
            max_area = area

print(max_area) # 4777967538
