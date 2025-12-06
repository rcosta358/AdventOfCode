def product(values: list[int]) -> int:
    res = 1
    for v in values:
        res *= v
    return res