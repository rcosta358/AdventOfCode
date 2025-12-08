from distance import *

with open("puzzle_input.txt") as f:
    lines = f.read().splitlines()

n = len(lines)
edges = [] 
for i in range(n):
    for j in range(i + 1, n):
        p1 = tuple(map(int, lines[i].split(',')))
        p2 = tuple(map(int, lines[j].split(',')))
        d = euclidean_distance(p1, p2)
        edges.append((d, i, j))

edges.sort()
circuits = [set([i]) for i in range(n)]
last_i = last_j = -1
for index in range(len(edges)):
    d, i, j = edges[index]

    # find circuits containing i and j
    ci = cj = set()
    for c in circuits:
        if i in c:
            ci = c
        if j in c:
            cj = c
        if ci and cj:
            break
    
    # if they are in different circuits, connect them
    if ci is not cj:
        ci.update(cj)
        circuits.remove(cj)

        # stop when all in the same circuit
        if len(circuits) == 1:
            last_i, last_j = i, j
            break

p1_x = int(lines[last_i].split(',')[0])
p2_x = int(lines[last_j].split(',')[0])
res = p1_x * p2_x

print(res) # 9617397716
