from collections import deque

def check(expected, actual):    
    if actual == expected:
        print(actual, 'OK')
    else:
        print(f'{actual} != {expected} ERROR')

def open_files(input_file, output_file):
    start_values = []
    with open(input_file) as f:
        for line in f.read().splitlines():
            line_split = line.split(' ')
            last_split_element = line_split[-1]
            last_split_element_int = int(last_split_element)
            start_values.append(last_split_element_int)

    with open(output_file) as f:
        output_values = list(map(int, f.read().splitlines()))

    return start_values, output_values

def step(value, factor, modulus):
    p = value * factor
    pm = p % modulus
    return pm


def get_low_16_bit(value):
    value_bin = '{:032b}'.format(value)
    value_bin_low = value_bin[16:]
    return value_bin_low

def main():
    start_values, output_values = open_files('day15.input', 'day15.output')

    val_a = start_values[0]
    val_b = start_values[1]
    factor_a = 16807
    factor_b = 48271
    modulus = 2147483647

    n_part_1 = 0
    n_part_2 = 0
    deque_a = deque()
    deque_b = deque()
    pair_count = 0
    for i in range(40000000):
        val_a = step(val_a, factor_a, modulus)
        val_a_bin_low = get_low_16_bit(val_a)
        
        val_b = step(val_b, factor_b, modulus)
        val_b_bin_low = get_low_16_bit(val_b)

        if val_a_bin_low == val_b_bin_low:
            n_part_1 += 1

        if pair_count <= 5000000:

            if val_a % 4 == 0:
                deque_a.append(val_a)

            if val_b % 8 == 0:
                deque_b.append(val_b)

            if deque_a and deque_b:
                pair_count += 1

                cmp_val_a = deque_a.popleft()
                cmp_val_b = deque_b.popleft()

                cmp_val_a_bin_low = get_low_16_bit(cmp_val_a)
                cmp_val_b_bin_low = get_low_16_bit(cmp_val_b)

                if cmp_val_a_bin_low == cmp_val_b_bin_low:
                    n_part_2 += 1

    check(output_values[0], n_part_1)
    check(output_values[1], n_part_2)

if __name__ == '__main__':
    main()