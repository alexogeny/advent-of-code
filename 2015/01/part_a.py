def input() -> str:
    with open('2015/01/input.txt', 'r') as f:
        return f.read()

def main():
    input_str = input()
    return input_str.count('(') - input_str.count(')')

if __name__ == "__main__":
    print(main())
