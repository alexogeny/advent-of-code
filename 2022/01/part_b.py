def input() -> str:
    with open('input.txt', 'r') as f:
        return f.read()

def main():
    input_str = input()
    elves = {}
    current_elf = 1
    for line in input_str.splitlines():
        if line.isdigit():
            elves[current_elf] = elves.get(current_elf, 0) + int(line)
        else:
            current_elf += 1
    
    max_elves = sorted(elves, key=elves.get, reverse=True)[:3]
    return sum(elves[elf] for elf in max_elves)


if __name__ == "__main__":
    print(main())
