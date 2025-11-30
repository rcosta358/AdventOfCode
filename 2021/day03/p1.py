with open("puzzle_input.txt") as f:
    lines = f.read().splitlines()

gamma = "" # most common bits
epsilon = "" # least common bits

for col in zip(*lines): # group by column
    ones = col.count("1")
    zeros = col.count("0")
    gamma += "1" if ones > zeros else "0"
    epsilon += "0" if ones > zeros else "1"

power = int(gamma, 2) * int(epsilon, 2)
print(power) # 841526
