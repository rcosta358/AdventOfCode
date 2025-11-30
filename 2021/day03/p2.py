
def get_winning_bit(word: str, bit: str) -> str:
    ones = word.count("1")
    zeros = word.count("0")
    other = "1" if bit == "0" else "0"
    return bit if ones >= zeros else other

def get_rating(candidates: list[str], bit: str) -> int:
    for i in range(len(candidates[0])):
        if len(candidates) == 1:
            break

        columns = [''.join(col) for col in zip(*candidates)]
        winning_bit = get_winning_bit(columns[i], bit)
        candidates = [c for c in candidates if c[i] == winning_bit]
    
    return int(candidates[0], 2)

with open("puzzle_input.txt") as f:
    lines = f.read().splitlines()

o2 = get_rating(lines, "1")
co2 = get_rating(lines, "0")
result = o2 * co2
print(result) # 4790390
