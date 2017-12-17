def open_files(input_file, output_file):
    with open(input_file) as f:
        lines = f.read().splitlines()
        inputs = []
        for line in lines:
            s = line.split(' ')
            step_len = int(s[0])
            iterations = int(s[1])
            inputs.append((step_len, iterations))

    with open(output_file) as f:
        outputs = list(map(int, f.read().splitlines()))

    return inputs, outputs

def part_1(step_len, iterations):
    buffer = [0]
    pos = 0
    n = 0

    for iter in range(iterations):
        pos = (pos + step_len) % len(buffer)
        n += 1
        pos += 1
        buffer.insert(pos, n)

    after_pos = buffer[(pos+1)%len(buffer)]

    # zero_index = buffer.index(0) if 0 in buffer else None
    # if zero_index is not None:
    #     after_zero = buffer[(zero_index+1)%len(buffer)]
    # else:
    #     after_zero = None
    # return after_pos, after_zero
    
    return after_pos

def part_2(step_len, iterations):
    insered_after_zero = None

    pos = 0
    n = 0
    for _ in range(iterations):
        n += 1
        pos = (pos + step_len) % n
        pos += 1

        if pos == 1:
            insered_after_zero = n

    return insered_after_zero


def check(expected, actual):    
    if actual == expected:
        print(actual, 'OK')
    else:
        print(f'{actual} != {expected} ERROR')
        
def main():
    inputs, outputs = open_files('day17.input', 'day17.output')
    
    input_1 = inputs[0]
    output_1 = outputs[0]
    result_1 = part_1(input_1[0], input_1[1])
    check(output_1, result_1)

    input_2 = inputs[1]
    output_2 = outputs[1]
    result_2 = part_2(input_2[0], input_2[1])
    check(output_2, result_2)

if __name__ == '__main__':
    main()