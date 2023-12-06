'''
Day 6 Problem
'''

EXAMPLE_FILE = "example.txt"
INPUT_FILE = "input.txt"

def read_races(file):
    with open(file, 'r', encoding='utf-8') as f:
        lines =  [int(y.strip()) for x in [(x.strip()).split(":")[-1] for x in f.readlines()] for y in x.split()]
        races = []
        n = len(lines)
        for i in range(n//2):
            races.append({
                "time": lines[i],
                "distance": lines[n//2 + i],
            })
        return races

def calculate_valid_start_points(race):
    counts = 0
    for button_pressed_duration in range(0, race['time']):
        distance_moved_by_boat = button_pressed_duration * (race['time'] - button_pressed_duration)
        if distance_moved_by_boat > race['distance']:
            counts += 1
    return counts

def part1(file):
    races = read_races(file)
    answer = 1
    for race in races:
        answer *= calculate_valid_start_points(race)
    return answer

def part2(file):
    races = read_races(file)
    
    # combine races
    main_race = {"time":"", "distance": ""}

    for race in races:
        main_race['time'] = main_race['time'] + str(race['time'])
        main_race['distance'] = main_race['distance'] + str(race['distance'])
    
    main_race['time'] = int(main_race['time'])
    main_race['distance'] = int(main_race['distance'])

    return calculate_valid_start_points(main_race)


def main():
    '''Main Program'''
    print("Part 1 Answer:", part1(INPUT_FILE))

    assert part2(EXAMPLE_FILE) == 71503
    print("Part 2 Answer:", part2(INPUT_FILE))

if __name__ == "__main__":
    main()
