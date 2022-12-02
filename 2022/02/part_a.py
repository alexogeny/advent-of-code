import re

def input() -> str:
    with open('input.txt', 'r') as f:
        return f.read()

def rockoff_map(input: str) -> int:
    return {
        "A": 1,
        "B": 2,
        "C": 3,
        "X": 1,
        "Y": 2,
        "Z": 3,
    }[input]

def compute_score(opponent: str, player: str) -> int:
    base = rockoff_map(player)
    if (opponent, player) in [("A", "Y"), ("B", "Z"), ("C", "X")]:
        return 6 + base
    if (opponent, player) in [("A", "X"), ("B", "Y"), ("C", "Z")]:
        return 3 + base
    if (opponent, player) in [("A", "Z"), ("B", "X"), ("C", "Y")]:
        return base

def main():
    input_str = input()
    total_score = 0
    r = re.compile(r'(?P<opponent>\w)\s(?P<player>\w)')
    for line in input_str.splitlines():
        if line:
            match = r.search(line)
            total_score += compute_score(match.group('opponent'), match.group('player'))
    return total_score

if __name__ == "__main__":
    print(main())
