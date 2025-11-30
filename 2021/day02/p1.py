with open("puzzle_input.txt") as f:
    horizontal = 0
    depth = 0
    for line in f.readlines():
        sep = line.split(" ")
        val = int(sep[1])
        match sep[0]:
            case "forward":
                horizontal += val
            case "up":
                depth -= val
            case "down":
                depth += val

    print(horizontal * depth) # 2027977