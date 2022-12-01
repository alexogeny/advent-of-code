def input() -> str:
    with open('2015/01/input.txt', 'r') as f:
        return f.read()

def main():
    input_str = input()
    flipper = [{'(': +1, ')': -1}[char] for char in input_str]
    matching_indices = (
        idx
        for idx, _step
        in enumerate(flipper)
        if sum(flipper[0:idx]) < 0
    )
    return next(matching_indices)

if __name__ == "__main__":
    print(main())
