with open("puzzle_input.txt") as f:
    lines = f.read().splitlines()

def flip(diagram: str, button: list[int]):
    d = list(diagram)
    for i in button:
        d[i] = '.' if d[i] == '#' else '#'
    return ''.join(d)

INFINITY = float('inf')
res = 0
for line in lines:
    split = line.split(' ')
    diagram = split[0].strip('[]')
    buttons = [list(map(int, b.strip('()').split(','))) for b in split[1:-1]]
    n = len(buttons)
    initial_lights = '.' * len(diagram)
    min_presses = INFINITY

    def find(lights: str, button: int = 0, presses: int = 0):
        global min_presses
        if presses >= min_presses:
            return # prune search
        
        if button == n:
            if lights == diagram:
                min_presses = presses
            return
        
        # explore both options
        find(lights, button + 1, presses) # dont press
        new_lights = flip(lights, buttons[button])
        find(new_lights, button + 1, presses + 1) # press
    
    find(initial_lights)
    if min_presses != INFINITY:
        res += min_presses

print(res) # 404
