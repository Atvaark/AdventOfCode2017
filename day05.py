def read_ints(path):
    with open(path) as f:
        return list(map(int, f.read().splitlines()))

def calc_steps(instructions, part):
    step_count = 0
    offset = 0
    while offset >= 0 and offset < len(instructions):
        instruction = instructions[offset]        

        if part == 1:
            instructions[offset] = instruction + 1
        elif part == 2:
            if instruction >= 3:
                instructions[offset] = instruction - 1
            else:
                instructions[offset] = instruction + 1

        offset += instruction
        step_count += 1

    return step_count

def check(expected, actual):    
    if actual == expected:
        print(actual, 'OK')
    else:
        print(f'{actual} != {expected} ERROR')

def main():
    instructions = read_ints('day05.input')
    outputs = read_ints('day05.output')
    
    expected1 = outputs[0]
    actual1 = calc_steps(list(instructions), 1)
    check(expected1, actual1)

    expected2 = outputs[1]
    actual2 = calc_steps(list(instructions), 2)
    check(expected2, actual2)

if __name__ == '__main__':
    main()