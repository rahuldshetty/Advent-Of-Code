'''
--- Day 1: Trebuchet?! ---

Something is wrong with global snow production, and you've been selected to take a look. The Elves have even given you a map; on it, they've used stars to mark the top fifty locations that are likely to be having problems.

You've been doing this long enough to know that to restore snow operations, you need to check all fifty stars by December 25th.

Collect stars by solving puzzles. Two puzzles will be made available on each day in the Advent calendar; the second puzzle is unlocked when you complete the first. Each puzzle grants one star. Good luck!

You try to ask why they can't just use a weather machine ("not powerful enough") and where they're even sending you ("the sky") and why your map looks mostly blank ("you sure ask a lot of questions") and hang on did you just say the sky ("of course, where do you think snow comes from") when you realize that the Elves are already loading you into a trebuchet ("please hold still, we need to strap you in").

As they're making the final adjustments, they discover that their calibration document (your puzzle input) has been amended by a very young Elf who was apparently just excited to show off her art skills. Consequently, the Elves are having trouble reading the values on the document.

The newly-improved calibration document consists of lines of text; each line originally contained a specific calibration value that the Elves now need to recover. On each line, the calibration value can be found by combining the first digit and the last digit (in that order) to form a single two-digit number.

--- Part Two ---

Your calculation isn't quite right. It looks like some of the digits are actually spelled out with letters: one, two, three, four, five, six, seven, eight, and nine also count as valid "digits".

Equipped with this new information, you now need to find the real first and last digit on each line. For example:
'''

# word size: 3, 4, 5

words = {
    "one": "o1e",
    "two": "t2o",
    "three": "t3e",
    "four": "f4r",
    "five": "f5e",
    "six": "s6",
    "seven": "s7n",
    "eight": "e8t",
    "nine": "n9e"
}

def find_callibration_value(input_str):
    n =  len(input_str) 
    i, j = 0, n - 1
    
    while i < n and not input_str[i].isdigit():
        i += 1
    
    while j >= 0 and not input_str[j].isdigit():
        j -= 1

    return int(input_str[i] + input_str[j])

def main1(file):
    with open(file, 'r') as f:
        inputs = [x.strip() for x in f.readlines()]
    
    if len(inputs) == 0:
        return 0

    return sum(
        find_callibration_value(x) for x in inputs
    )



def find_spelled_callibration_value(input_str:str):
    # Change existing entries for the string
    for digit in words:
        if digit in input_str:
            input_str = input_str.replace(digit, (words[digit]))

    n =  len(input_str) 
    i, j = 0, n - 1
    
    while i < n and not input_str[i].isdigit():
        i += 1
    
    while j >= 0 and not input_str[j].isdigit():
        j -= 1

    return int(input_str[i] + input_str[j])

def main2(file):
    with open(file, 'r') as f:
        inputs = [x.strip() for x in f.readlines()]
    
    if len(inputs) == 0:
        return 0

    return sum(
        find_spelled_callibration_value(x) for x in inputs
    )


if __name__ == '__main__':
    print("Part1 - Answer:", main1('input.txt'))

    print("Part2 - Answer:", main2('input.txt'))
