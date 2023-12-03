'''

--- Day 3: Gear Ratios ---

You and the Elf eventually reach a gondola lift station; he says the gondola lift will take you up to the water source, but this is as far as he can bring you. You go inside.

It doesn't take long to find the gondolas, but there seems to be a problem: they're not moving.

"Aaah!"

You turn around to see a slightly-greasy Elf with a wrench and a look of surprise. "Sorry, I wasn't expecting anyone! The gondola lift isn't working right now; it'll still be a while before I can fix it." You offer to help.

The engineer explains that an engine part seems to be missing from the engine, but nobody can figure out which one. If you can add up all the part numbers in the engine schematic, it should be easy to work out which part is missing.

The engine schematic (your puzzle input) consists of a visual representation of the engine. There are lots of numbers and symbols you don't really understand, but apparently any number adjacent to a symbol, even diagonally, is a "part number" and should be included in your sum. (Periods (.) do not count as a symbol.)

Here is an example engine schematic:

467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..

In this schematic, two numbers are not part numbers because they are not adjacent to a symbol: 114 (top right) and 58 (middle right). Every other number is adjacent to a symbol and so is a part number; their sum is 4361.

Of course, the actual engine schematic is much larger. What is the sum of all of the part numbers in the engine schematic?


--- Part Two ---

The engineer finds the missing part and installs it in the engine! As the engine springs to life, you jump in the closest gondola, finally ready to ascend to the water source.

You don't seem to be going very fast, though. Maybe something is still wrong? Fortunately, the gondola has a phone labeled "help", so you pick it up and the engineer answers.

Before you can explain the situation, she suggests that you look out the window. There stands the engineer, holding a phone in one hand and waving with the other. You're going so slowly that you haven't even left the station. You exit the gondola.

The missing part wasn't the only issue - one of the gears in the engine is wrong. A gear is any * symbol that is adjacent to exactly two part numbers. Its gear ratio is the result of multiplying those two numbers together.

This time, you need to find the gear ratio of every gear and add them all up so that the engineer can figure out which gear needs to be replaced.

Consider the same engine schematic again:

467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..

In this schematic, there are two gears. The first is in the top left; it has part numbers 467 and 35, so its gear ratio is 16345. The second gear is in the lower right; its gear ratio is 451490. (The * adjacent to 617 is not a gear because it is only adjacent to one part number.) Adding up all of the gear ratios produces 467835.

What is the sum of all of the gear ratios in your engine schematic?


'''
file = 'input.txt'

dirs = [(1, 0), (0, 1), (-1, 0), (0, -1), (1,1), (1, -1), (-1, 1), (-1, -1)]

def read_input():
    with open(file, 'r') as f:
        return [x.strip() + "." for x in f.readlines()]

def valid_symbol(c):
    return c != "." and not c.isdigit()

def check_neighbor_for_valid_symbol(x, y, M):
    rows, cols = len(M), len(M[0])
    for dx, dy in dirs:
        new_x, new_y = x + dx, y + dy
        if 0 <= new_x < rows and 0 <= new_y < cols:
            if valid_symbol(M[new_x][new_y]):
                return True
    return False


def par1(M):
    res = 0

    rows, cols = len(M), len(M[0])
    
    temp = 0
    valid = False

    for i in range(rows):
        for j in range(cols):
            if M[i][j].isdigit():
                temp = temp * 10 + int(M[i][j])
                # print(temp)
                if check_neighbor_for_valid_symbol(i, j, M):
                    valid = True
            else:
                if temp != 0 and valid:
                    res += temp
                temp = 0
                valid = False

        # if temp != 0 and valid:
        #     res += temp

    return res


def find_number(x, y, M):
    cols = len(M[0])
    s = ""

    i = y
    while i >= 0 and M[x][i].isdigit():
        s = M[x][i]  + s 
        M[x][i]  = "."
        i -= 1
    
    i = y + 1
    while i < cols and M[x][i].isdigit():
        s = s + M[x][i]
        M[x][i]  = "."
        i += 1

    return int(s)


def find_gear_ratio(i, j, M):
    rows, cols = len(M), len(M[0])
    
    gear_ratio = 1
    count = 0

    for dx, dy in dirs:
        x, y = i + dx, j + dy
        if 0 <= x < rows and 0 <= y < cols and M[x][y].isdigit():
            gear_ratio *= find_number(x, y, M)
            count += 1

    return gear_ratio if count == 2 else 0 
        


def part2(M):
    M = [list(x) for x in M]
    rows, cols = len(M), len(M[0])

    sum_of_gear_ratios = 0

    for i in range(rows):
        for j in range(cols):
            if M[i][j] == "*":
                sum_of_gear_ratios += find_gear_ratio(i, j, M)

    return sum_of_gear_ratios

def main():
    M = read_input()
    print("Part 1 Result:", par1(M))
    print("Part 2 Result:", part2(M))

if __name__ == "__main__":
    main()