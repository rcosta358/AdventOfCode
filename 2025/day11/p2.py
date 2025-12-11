from functools import cache

with open("puzzle_input.txt") as f:
    lines = f.read().splitlines()

paths = {}
for line in lines:
    src, rest = line.split(": ")
    dst = rest.split(" ")
    paths[src] = dst

target_seen = {"fft", "dac"}

@cache
def count_paths(curr: str, end: str, seen: int = 0) -> int:
    if curr in target_seen:
        seen += 1
    if curr == end:
        return 1 if seen == len(target_seen) else 0 # only count if all targets seen
    
    return sum(count_paths(n, end, seen) for n in paths[curr])

res = count_paths("svr", "out")
print(res) # 331837854931968
