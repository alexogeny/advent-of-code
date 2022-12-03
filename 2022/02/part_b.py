import re

def input() -> str:
    with open('input.txt', 'r') as f:
        return f.read()

def rotate(direction: int, rps: str = "rps") -> str:
    rps = rps[direction:3] + rps[0:direction]
    return rps

def compute_score(opponent, player):
    opponent_pos, player_pos = "ABC".index(opponent), "XYZ".index(player)-1
    rps = rotate(opponent_pos)
    rps = rotate(player_pos, rps)
    player_rps = rps[0]
    return 1 + "rps".index(player_rps) + "XYZ".index(player)*3

def tests():
    assert compute_score("A", "Y") == 4
    assert compute_score("B", "X") == 1
    assert compute_score("C", "Z") == 7

def main():
    tests()
    input_str = input()
    total_score = 0
    r = re.compile(r'(?P<opponent>\w)\s(?P<player>\w)')
    for line in input_str.splitlines():
        if line:
            match = r.search(line)
            opponent, player = match.group('opponent'), match.group('player')
            total_score += compute_score(opponent, player)

    return total_score

if __name__ == "__main__":
    print(main())
