with open("puzzle_input.txt") as f:
    lines = f.read().splitlines()

res = 0
for line in lines:
    first = 1
    split_index = -1
    for i in range(len(line) - 1):
        val = int(line[i])
        if val > first:
            first = val
            split_index = i
        
    second = 1
    for i in range(split_index + 1, len(line)):
        val = int(line[i])
        if val > second:
            second = val
    
    res += int(str(first) + str(second))

print(res) # 17321
