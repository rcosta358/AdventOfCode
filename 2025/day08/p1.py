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
for index in range(1000):
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

circuit_sizes = sorted([len(c) for c in circuits], reverse=True)
res = circuit_sizes[0] * circuit_sizes[1] * circuit_sizes[2]

print(res) # 352584
