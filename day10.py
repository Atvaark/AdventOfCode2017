def run(lengths, num_rounds, suffix):
    num_list = list(range(256))
    lengths += suffix

    cur_pos = 0
    skip_size = 0
    for _ in range(num_rounds):   
        for length in lengths:
            len1 = (cur_pos+length) % len(num_list)
            if len1 > 0 and len1 < length:
                len2 = length - len1
                len_slice2 = num_list[cur_pos:cur_pos+len2]
                len_slice1 = num_list[:len1]
                len_slice = len_slice2 + len_slice1
                len_slice_rev = len_slice[::-1]
                num_list[cur_pos:cur_pos+len2] = len_slice_rev[:len2]
                num_list[:len1] = len_slice_rev[len2:]
            else:
                len_slice = num_list[cur_pos:cur_pos+length]
                len_slice_rev = len_slice[::-1]
                num_list[cur_pos:cur_pos+length] = len_slice_rev

            cur_pos = (cur_pos + length + skip_size) % len(num_list)

            skip_size += 1

    result1 = num_list[0]*num_list[1]

    hash = []
    for i in range(16):
        block = num_list[i*16:i*16+16]

        xor = 0
        for block_num in block:
            xor = xor ^ block_num

        hash.append(xor)
    hex_hash = ''.join('{:02x}'.format(x) for x in hash)

    return result1, hex_hash

def open_files(input_file, output_file):
    with open(input_file) as f:
        input_line = f.read().rstrip('\n')

    lengths1 = []
    for s in input_line.split(','):
        lengths1.append(int(s))

    lengths2 = [ord(x) for x in input_line]

    with open(output_file) as f:
        output_lines = f.read().splitlines()

    output1 = int(output_lines[0])
    output2 = output_lines[1]

    return lengths1, lengths2, output1, output2

def check(expected, actual):    
    if actual == expected:
        print(actual, 'OK')
    else:
        print(f'{actual} != {expected} ERROR')

def main():
    i1, i2, o1, o2 = open_files('day10.input', 'day10.output')

    result1, _ = run(i1, 1, [])
    check(o1, result1)

    _, result2 = run(i2, 64, [17, 31, 73, 47, 23])
    check(o2, result2)


if __name__ == '__main__':
    main()