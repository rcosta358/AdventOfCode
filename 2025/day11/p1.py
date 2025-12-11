with open("puzzle_input.txt") as f:
    lines = f.read().splitlines()

paths = {}
for line in lines:
    src, rest = line.split(": ")
    dst = rest.split(" ")
    paths[src] = dst

def count_paths(curr: str, end: str) -> int:
    if curr == end:
        return 1
    
    return sum(count_paths(n, end) for n in paths[curr])

res = count_paths("you", "out")
print(res) # 566
