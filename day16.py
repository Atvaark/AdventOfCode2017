def read_files(input_file, output_file):
    with open(input_file) as f:
        raw_steps = f.read().rstrip().split(',')

    steps = []
    for raw_step in raw_steps:
        step_type = raw_step[0]
        if step_type == 's':
            n = int(raw_step[1:])
            steps.append((step_type, n))
        elif step_type == 'x':
            positions = list(map(int, raw_step[1:].split('/')))
            steps.append((step_type, positions))
        elif step_type == 'p':
            partners = raw_step[1:].split('/')
            steps.append((step_type, partners))

    with open(output_file) as f:
        output_orders = f.read().splitlines()
            
    return steps, output_orders

def swap_programs(programs, idx_1, idx_2):
    p1 = programs[idx_1]
    p2 = programs[idx_2]
    programs = programs[:idx_2] + p1 + programs[idx_2 + 1:]
    programs = programs[:idx_1] + p2 + programs[idx_1 + 1:]
    return programs

def run(programs, steps):
    # print(programs)

    for step in steps:
        # print(step)
        if step[0] == 's':
            n = step[1]
            idx = len(programs) - n
            half_1 = programs[:idx]
            half_2 = programs[idx:]
            programs = half_2 + half_1
        elif step[0] == 'x':
            positions = step[1]
            programs = swap_programs(programs, positions[0], positions[1])
        elif step[0] == 'p':
            partners = step[1]
            partner_1_idx = programs.index(partners[0])
            partner_2_idx = programs.index(partners[1])
            programs = swap_programs(programs, partner_1_idx, partner_2_idx)
        # print(programs)

    return programs

def check(expected, actual):    
    if actual == expected:
        print(actual, 'OK')
    else:
        print(f'{actual} != {expected} ERROR')

def main():
    steps, output_orders = read_files('day16.input', 'day16.output')
    programs = 'abcdefghijklmnop'

    known_orders = {}

    maxi = 1000000000
    i = 0
    found_loop = False

    part_1 = None
    while i < maxi:
        programs = run(programs, steps)
        if i == 0:
            part_1 = programs

        if not found_loop and programs in known_orders:
            other_i = known_orders[programs]
            diff = i - other_i
            final_loop_index = int(maxi / diff) * diff
            i = final_loop_index

            found_loop = True
        else:
            known_orders[programs] = i

        i += 1

    part_2 = programs

    check(output_orders[0], part_1)
    check(output_orders[1], part_2)

if __name__ == '__main__':
    main()