with open("puzzle_input.txt") as f:
    lines = f.read().splitlines()

res = 0
target_len = 12
for line in lines:
    val = line
    while len(val) > target_len:
        for i in range(len(val) - 1):
            if val[i] < val[i + 1]:
                val = val[:i] + val[i + 1:] # remove val[i]
                break
        else:
            # remove last char if none was removed
            val = val[:-1]

    res += int(val)

print(res) # 171989894144198
