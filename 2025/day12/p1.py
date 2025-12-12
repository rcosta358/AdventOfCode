from shapes import *

with open("puzzle_input.txt") as f:
    lines = f.read().split('\n\n')

shapes = []
for line in lines[:-1]:
    l = line.splitlines()
    index = int(l[0].strip(":"))
    shape = l[1:]
    shapes.append((index, shape))

regions = []
for line in lines[-1].splitlines():
    dim, parts = line.split(": ")
    w, h = map(int, dim.split("x"))
    parts = [int(p) for p in parts.split(" ")]
    regions.append((w, h, parts))

res = 0
for w, h, parts in regions:
    grid = ['.' * w for _ in range(h)]
    all_shapes = []
    for index, amount in enumerate(parts):
        for _ in range(amount):
            all_shapes.append(shapes[index])
    
    orientations = [get_orientations(shape) for _, shape in all_shapes]
    if can_place_shapes(grid, all_shapes, orientations):
        res += 1
        
print(res) # 546
