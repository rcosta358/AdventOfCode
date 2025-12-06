from product import product

with open("puzzle_input.txt") as f:
    lines = [[i for i in l.split(' ') if i != ''] for l in f.read().splitlines()]

res = 0
for x in range(len(lines[0])):
    values = [int(lines[y][x]) for y in range(len(lines)-1)]
    op = lines[-1][x]
    res += sum(values) if op == '+' else product(values)

print(res) # 4405895212738
    
