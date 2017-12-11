def get_distance(pos):
    pos_step = (0, 0)
    short_step_count = 0
    while pos[0] != pos_step[0] or pos[1] != pos_step[1]:
        if pos[0] == pos_step[0]:
            if pos[1] < pos_step[1]:
                pos_step = (pos_step[0], pos_step[1]-2)
            else:
                pos_step = (pos_step[0], pos_step[1]+2)
        elif pos[0] < pos_step[0]:
            if pos[1] < pos_step[1]:
                pos_step = (pos_step[0]-1, pos_step[1]-1)
            else:
                pos_step = (pos_step[0]-1, pos_step[1]+1)
        else:
            if pos[1] < pos_step[1]:
                pos_step = (pos_step[0]+1, pos_step[1]-1)
            else:
                pos_step = (pos_step[0]+1, pos_step[1]+1)
        
        short_step_count += 1

    return short_step_count

def open_files(input_file, output_file):
    input_file = 'day11.input'
    with open(input_file) as f:
        steps = f.read().rstrip('\n').split(',')

    with open(output_file) as f:
        output = list(map(int, f.read().splitlines()))

    return steps, output

def run(steps):
    pos = (0, 0)
    dirmap =  {
        'n': (0, 2),
        'ne': (1, 1),
        'se': (1, -1),
        's': (0, -2),
        'sw': (-1, -1),
        'nw': (-1, 1),
    }

    max_distance = 0
    for step in steps:
        offset = dirmap[step]
        pos = (pos[0] + offset[0], pos[1] + offset[1])

        max_distance = max(max_distance, get_distance(pos))

    short_step_count = get_distance(pos)

    return short_step_count, max_distance

def check(expected, actual):    
    if actual == expected:
        print(actual, 'OK')
    else:
        print(f'{actual} != {expected} ERROR')

def main():
    steps, output = open_files('day11.input', 'day11.output')

    short_step_count, max_distance = run(steps)

    check(output[0], short_step_count)
    check(output[1], max_distance)
    
if __name__ == '__main__':
    main()