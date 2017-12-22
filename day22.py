from copy import deepcopy

def run_part_1(infection_map, virus_pos, iterations):
    infect_count = 0
    direction = 0
    direction_offsets = [
        (0, -1), # up
        (1, 0), # right
        (0, 1), # down
        (-1, 0) # left
    ]

    for i in range(iterations):

        if virus_pos in infection_map:
            infection_map.remove(virus_pos) # clean
            direction = (direction + 1) % len(direction_offsets) # right
        else:
            infection_map.add(virus_pos) # infect
            direction = (direction - 1) % len(direction_offsets) # left
            infect_count += 1
        
        virus_offset = direction_offsets[direction]
        virus_pos = (
            virus_pos[0] + virus_offset[0],
            virus_pos[1] + virus_offset[1]
        )
    return infect_count

def run_part_2(infection_set, virus_pos, iterations):
    infect_count = 0
    direction = 0
    direction_offsets = [
        (0, -1), # up
        (1, 0), # right
        (0, 1), # down
        (-1, 0) # left
    ]

    infection_map = dict.fromkeys(infection_set, '#')

    for i in range(iterations):
        if virus_pos in infection_map:
            cell = infection_map[virus_pos]
            if cell == 'W':
                infection_map[virus_pos] = '#' # infect
                infect_count += 1
                # no turn
            elif cell == '#':
                infection_map[virus_pos] = 'F' # flag
                direction = (direction + 1) % len(direction_offsets) # right
            elif cell == 'F':
                del infection_map[virus_pos]  # clean
                direction = (direction + 2) % len(direction_offsets) # reverse

        else:
            infection_map[virus_pos] = 'W' # weaken
            direction = (direction - 1) % len(direction_offsets) # left
        
        virus_offset = direction_offsets[direction]
        virus_pos = (
            virus_pos[0] + virus_offset[0],
            virus_pos[1] + virus_offset[1]
        )
    return infect_count

def read_files(input_file, output_file):
    with open(input_file) as f:
        lines = f.read().splitlines()

    center_pos = None
    infection_map = set()
    for y_idx, line in enumerate(lines):
        width = len(line)
        if center_pos is None:
            center_pos = (
                (width-1)/2,
                (width-1)/2
            )

        for x_idx, cell in enumerate(line):
            if cell == '#':
                cell_pos = (
                    x_idx - center_pos[0],
                    y_idx - center_pos[1]
                )

                infection_map.add(cell_pos)

    center_pos = (0, 0)

    with open(output_file) as f:
        outputs = list(map(int, f.read().splitlines()))

    return infection_map, center_pos, outputs

def check(expected, actual):    
    if actual == expected:
        print(actual, 'OK')
    else:
        print(f'{actual} != {expected} ERROR')

def main():
    input_file = 'day22.input'
    output_file = 'day22.output'
    infection_set, virus_pos, outputs = read_files(input_file, output_file)
    infect_count_1 = run_part_1(deepcopy(infection_set), virus_pos, 10000)
    check(outputs[0], infect_count_1)
    
    infect_count_2 = run_part_2(deepcopy(infection_set), virus_pos, 10000000)
    check(outputs[1], infect_count_2)
if __name__ == '__main__':
    main()