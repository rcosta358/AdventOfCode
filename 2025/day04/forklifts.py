def count_adjacent(x: int, y: int, lines: list[str]) -> int:
    count = 0
    for dx in (-1, 0, 1):
        for dy in (-1, 0, 1):
            if (dx, dy) == (0, 0):
                continue
            nx, ny = x + dx, y + dy
            if 0 <= nx < len(lines[0]) and 0 <= ny < len(lines):
                if lines[ny][nx] != ".":
                    count += 1
    return count