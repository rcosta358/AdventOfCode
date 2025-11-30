with open("puzzle_input.txt") as f:
    horizontal = 0
    depth = 0
    aim = 0
    for line in f.readlines():
        sep = line.split(" ")
        val = int(sep[1])
        match sep[0]:
            case "forward":
                horizontal += val
                depth += aim * val
            case "up":
                aim -= val
            case "down":
                aim += val

    print(horizontal * depth) # 1903644897