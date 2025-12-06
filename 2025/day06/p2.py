from product import product

with open("puzzle_input.txt") as f:
    lines = f.read().splitlines()

res = 0
values = []
for col in range(len(lines[0])-1, -1, -1):
    digits = ''
    for line in range(len(lines)):
        val = lines[line][col]
        if val.isdigit():
            digits += val     
        else:
            if digits != '':
                values.append(int(digits))
                digits = ''
            if val != ' ':
                res += sum(values) if val == '+' else product(values)
                values.clear()

print(res) # 7450962489289