'''
Day 5 Challenge: Advent of Code

See problem.txt for Problem Statement.
'''
from multiprocessing import Pool

EXAMPLE_INPUT_FILE = "example.txt"
TEST_INPUT_FILE = "input.txt"

EXAMPLE_PART1_ANSWER = 35
EXAMPLE_PART2_ANSWER = 46

class ProblemInput:
    def __init__(self, seeds=None, key_mappings=None, data_map=None):
        self.seeds = seeds
        self.key_mappings = key_mappings
        self.data_map = data_map

def read_input(file):
    '''
    seeds: 79 14 55 13

    seed-to-soil map:
    50 98 2
    52 50 48

    destination_range_start source_range_start no_of_values
    First line mapping:{
        98: 50,
        99: 51
    }

    Second line mapping:{
        50: 52,
        51: 53,
        .
        .
        .
        97: 99
    }

    In the first example:
    Seed 79 corresponds to Soil: 81 
        a: (79 - 50) = 29
        b: a + 52 =  81

    any other numbers not specified refers to the same number.
    '''
    with open(file, 'r', encoding='utf-8') as f:
        problem_input = ProblemInput()
        input_str = [x.strip() for x in f.readlines() if len(x.strip()) > 0]

        # Extract input seeds line
        num_line = input_str[0].split(":")[-1]
        problem_input.seeds = [int(x) for x in num_line.split()]

        # Extract Mappings
        data_map = {}
        key_mappings = {}
        temp_key = None
        temp_items = []
        for line in input_str[1:]:
            if line[0].isalpha():
                # Process mapping line
                src, dest = (line.split()[0]).split("-to-")
                key_mappings[src] = dest

                if len(temp_items) > 0:
                    data_map[temp_key] = temp_items.copy()
                    temp_items = []
                
                temp_key = src

            else:
                # Process number mapping
                dest, source, values = [int(x) for x in line.split()]
                temp_items.append((dest, source, values))

        if len(temp_items) > 0:
            data_map[temp_key] = temp_items

        problem_input.data_map = data_map
        problem_input.key_mappings = key_mappings
        return problem_input

def find_seed_location(seed, problem_input:ProblemInput):
    '''
    Traverse the seed mappings and find the location
    '''
    start = "seed"
    while start != 'location':
        range_lists = problem_input.data_map[start]

        for dst, src, val in range_lists:
            # Key range
            begin = src
            end = begin + val - 1
            if begin <= seed <= end:
                a = seed - src
                seed = a + dst
                break
        
        # Move to next mapping
        start = problem_input.key_mappings[start]

    return seed

def part1(file):
    '''
    Solution to the first problem
    '''
    problem_input = read_input(file)
    min_val = float('inf')
    for seed in problem_input.seeds:
        min_val = min(min_val, find_seed_location(seed, problem_input))

    return min_val

################
#################

def part2(file):
    '''
    Solution to the first problem
    '''
    problem_input = read_input(file)

    min_val = float('inf')

    n = len(problem_input.seeds)

    for i in range(0, n, 2):
        begin = problem_input.seeds[i]
        end = begin + problem_input.seeds[i + 1]
        for seed in range(begin, end):
            min_val = min(min_val, find_seed_location(seed, problem_input))

    return min_val

def main():
    '''
    Just a main program
    '''
    # assert part1(EXAMPLE_INPUT_FILE) == EXAMPLE_PART1_ANSWER
    # print("Part 1 Result:", part1(TEST_INPUT_FILE))
    assert part2(EXAMPLE_INPUT_FILE) == EXAMPLE_PART2_ANSWER
    print("Part 2 Result:", part2(TEST_INPUT_FILE))

if __name__ == "__main__":
    main()