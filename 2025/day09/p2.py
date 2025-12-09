from rect import *

with open("puzzle_input.txt") as f:
    lines = f.read().splitlines()

points = [tuple(map(int, line.split(','))) for line in lines]
bounds: dict[int, list[int]] = {} # y -> [min_x, max_x]
n = len(points)

for i in range(n - 1):
    p1 = points[i]
    p2 = points[i + 1]
    min_x, max_x = min(p1[0], p2[0]), max(p1[0], p2[0])
    min_y, max_y = min(p1[1], p2[1]), max(p1[1], p2[1])

    for y in range(min_y, max_y + 1):
        if y not in bounds:
            bounds[y] = [min_x, max_x]
        else:
            if min_x < bounds[y][0]:
                bounds[y][0] = min_x 
            if max_x > bounds[y][1]:
                bounds[y][1] = max_x

max_area = 0
for i in range(n):
    for j in range(i + 1, n):
        p1 = points[i]
        p2 = points[j]
    
        if not in_bounds(bounds, p1[0], p1[1], p2[0], p2[1]):
            continue
    
        area = rect_area(p1, p2)
        if area > max_area:
            max_area = area

print(max_area) # 1439894345
