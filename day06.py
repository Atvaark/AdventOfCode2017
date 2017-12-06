def check(expected, actual):    
    if actual == expected:
        print(actual, 'OK')
    else:
        print(f'{actual} != {expected} ERROR')

def open_files(in_path, out_path):
    with open(in_path) as f:
        banks = list(map(int, f.read().split('\t')))

    with open(out_path) as f:
        outputs = list(map(int, f.read().splitlines()))

    return banks, outputs

def realloc_banks(banks):
    states = {}
    state = "-".join(str(bank) for bank in banks)
    states[state] = 0

    cycles = 0
    cycle_size = 0
    while True:
        max_idx = 0
        max_val = 0
        for idx, val in enumerate(banks):
            if val > max_val:
                max_val = val
                max_idx = idx

        banks[max_idx] = 0
        idx = (max_idx + 1) % len(banks)
        for n in range(max_val):
            banks[idx] += 1
            idx = (idx + 1) % len(banks)

        cycles += 1
        
        state = "-".join(str(bank) for bank in banks)
        if state in states:
            cycle_size = cycles - states[state]
            break

        states[state] = cycles

    return cycles, cycle_size

def main():
    banks, outputs = open_files('day06.input', 'day06.output')
    
    cycles, cycle_size = realloc_banks(banks)

    check(outputs[0], cycles)
    check(outputs[1], cycle_size)

if __name__ == '__main__':
    main()