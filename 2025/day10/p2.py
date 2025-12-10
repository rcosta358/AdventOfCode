from z3 import *

with open("puzzle_input.txt") as f:
    lines = f.read().splitlines()

def solve_with_z3(buttons: list[list[int]], joltages: list[int]) -> int:
    opt = Optimize() 
    
    # define variables
    button_vars = [Int(f'b_{i}') for i in range(len(buttons))]

    # add constraints
    for b in button_vars:
        opt.add(b >= 0)

    n = len(joltages)
    for i in range(n):
        counter_sum = Sum([button_vars[j] for j, indices in enumerate(buttons) if i in indices])
        opt.add(counter_sum == joltages[i])

    # set objective
    opt.minimize(Sum(button_vars))

    # solve
    if opt.check() == sat:
        model = opt.model()
        return sum(model[b].as_long() for b in button_vars) # type: ignore
    else:
        raise Exception("No solution found")
    
res = 0
for line in lines:
    split = line.split(' ')
    buttons = [list(map(int, b.strip('()').split(','))) for b in split[1:-1]]
    joltages = list(map(int, split[-1].strip('{}').split(',')))
    res += solve_with_z3(buttons, joltages)

print(res) # 16474
