
def rect_area(p1: tuple, p2: tuple) -> int:
    width = abs(p1[0] - p2[0]) + 1
    height = abs(p1[1] - p2[1]) + 1
    return width * height

def in_bounds(bounds: dict, x1: int, y1: int, x2: int, y2: int) -> bool:
    curr_min_y, curr_max_y = min(y1, y2), max(y1, y2)
    curr_min_x, curr_max_x = min(x1, x2), max(x1, x2)

    for y in range(curr_min_y, curr_max_y + 1):
        if y not in bounds:
            return False
        
        min_x, max_x = bounds[y]
        if curr_min_x < min_x or curr_max_x > max_x:
            return False
            
    return True