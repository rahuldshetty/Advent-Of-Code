import numpy as np

INPUT_FILE = "input.txt"
EXAMPLE_FILE = "example.txt"

def read_input(file):
    '''read input from file'''
    with open(file, 'r', encoding='utf-8') as f:
        lines = [x.strip() for x in f.readlines()]
        input_lines = []
        for line in lines:
            input_lines += [[int(x) for x in line.split()]]
        return input_lines

def get_diff(line):
    out = np.diff(line)
    return line[-1] if all([o == 0 for o in out]) else line[-1] + get_diff(out)

def part1(file):
    '''Soln to part1'''
    input_data = read_input(file)
    return sum([get_diff(row) for row in input_data])

def part2(file):
    '''Soln to part2'''
    input_data = read_input(file)
    return sum([get_diff(np.flip(np.array(row))) for row in input_data])

def main():
    '''Program Start'''
    # assert part1(EXAMPLE_FILE) == 114
    # print("Part 1 Result:", part1(INPUT_FILE))

    print("Part 2 Result:", part2(INPUT_FILE))

if __name__ == "__main__":
    main()
