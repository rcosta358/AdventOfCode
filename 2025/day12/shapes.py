
def rotate(shape: list[str]) -> list[str]:
    return [''.join(row) for row in zip(*shape[::-1])]

def flip(shape: list[str]) -> list[str]:
    return [row[::-1] for row in shape]

def get_orientations(shape: list[str]) -> list[list[str]]:
    orientations = []
    curr = shape
    for _ in range(4):
        for v in [curr, flip(curr)]:
            orientations.append(v)
        curr = rotate(curr)
    return orientations

def can_place(grid: list[str], shape: list[str], row: int, col: int) -> bool:
    for r, shape_row in enumerate(shape):
        for c, char in enumerate(shape_row):
            if char == '#':
                grid_r, grid_c = row + r, col + c
                if grid_r >= len(grid) or grid_c >= len(grid[0]) or grid[grid_r][grid_c] != '.':
                    return False
    return True

def place(grid: list[str], shape: list[str], row: int, col: int) -> list[str]:
    new_grid = [list(row) for row in grid]
    for r, shape_row in enumerate(shape):
        for c, ch in enumerate(shape_row):
            if ch == '#':
                new_grid[row + r][col + c] = '#'
    return [''.join(row) for row in new_grid]

def get_shape_area(shape: list[str]) -> int:
    return sum(row.count('#') for row in shape)

def can_place_shapes(grid: list[str], shapes: list[tuple[int, list[str]]], orientations, index: int = 0) -> bool:
    if index >= len(shapes):
        return True # all shapes placed
    
    remaining_spaces = sum(row.count('.') for row in grid)
    needed_spaces = sum(get_shape_area(s[1]) for s in shapes[index:])
    if remaining_spaces < needed_spaces:
        return False # not enough space left
    
    for orientation in orientations[index]:
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if can_place(grid, orientation, r, c):
                    new_grid = place(grid, orientation, r, c)
                    if can_place_shapes(new_grid, shapes, orientations, index + 1):
                        return True
    return False
