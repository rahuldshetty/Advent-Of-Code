import re, math

EXTRACT_PATTERN = "([A-Z0-9]{3}) = \(([A-Z0-9]{3}), ([A-Z0-9]{3})\)"

EXAMPLE1_FILE = "example.txt"
EXAMPLE2_FILE = "example1.txt"
INPUT_FILE = "input.txt"

PART2_EXAMPLE = "example-part2.txt"

def read_input(file):
    with open(file, 'r', encoding='utf-8') as f:
        lines = [x.strip() for x in f.readlines()]
        
        sequence = lines[0]
        
        nodes = {}

        # process node to l/r mapping
        for line in lines[2:]:
            groups = re.findall(EXTRACT_PATTERN, line)[0]
            nodes[groups[0]] = [groups[1], groups[2]]

        return sequence, nodes

def part1(file):
    seq, nodes = read_input(file)

    seq_pointer = 0
    cur_node = 'AAA'
    steps = 0

    while cur_node != 'ZZZ':
        dir = seq[seq_pointer]
        if dir == 'L':
            cur_node = nodes[cur_node][0]
        else:
            cur_node = nodes[cur_node][1]
        seq_pointer = (seq_pointer + 1) % len(seq)
        steps += 1
    
    return steps


def check_if_all_nodes_end_in_Z(node_list):
    for node in node_list:
        if node[-1] != 'Z':
            return False
    return True


def move_nodes_in_dir(nodes, node_list, dir):
    for i in range(len(node_list)):
        if dir == 'L':
            node_list[i] =  nodes[node_list[i]][0]
        else:
            node_list[i] =  nodes[node_list[i]][1]

def part2(file):
    seq, nodes = read_input(file)

    cur_nodes = [node for node in nodes if node.endswith("A")]
    step_values = []
    
    for node in cur_nodes:
        seq_pointer = 0
        steps = 0
        while node[-1] != 'Z':
            dir = seq[seq_pointer]
            if dir == 'L':
                node = nodes[node][0]
            else:
                node = nodes[node][1]
            seq_pointer = (seq_pointer + 1) % len(seq)
            steps += 1
        step_values.append(steps)
    return math.lcm(*step_values)


def main():
    # assert part1(EXAMPLE1_FILE) == 2
    # assert part1(EXAMPLE2_FILE) == 6
    # print("Part 1 Result:", part1(INPUT_FILE))
    
    assert part2(PART2_EXAMPLE) == 6
    print("Part 2 Result:", part2(INPUT_FILE))

if __name__ == "__main__":
    main()
