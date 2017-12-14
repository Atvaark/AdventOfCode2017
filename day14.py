def get_hash(lengths_string):
    lengths = [ord(x) for x in lengths_string]
    # num_rounds = 1
    # suffix = []
    num_rounds = 64
    suffix = [17, 31, 73, 47, 23]
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

    hash = []
    for i in range(16):
        block = num_list[i*16:i*16+16]

        xor = 0
        for block_num in block:
            xor = xor ^ block_num

        hash.append(xor)
    hex_hash = ''.join('{:02x}'.format(x) for x in hash)

    return hex_hash

def open_files(input_file, output_file):
    with open(input_file) as f:
        input_key = f.read().rstrip()

    with open(output_file) as f:
        outputs = list(map(int, f.read().splitlines()))

    return input_key, outputs

def create_inputs(input_key):
    inputs = []
    for i in range(128):
        inputs.append(input_key + '-' + str(i))

    return inputs

def to_bin(hex):
    return '{:0128b}'.format(int(hex, 16))
    
def run(input_key):
    row_keys = create_inputs(input_key)

    used_squares = 0
    region_count = 0
    
    grid = [0] * 128 * 128
    for row_idx, row_key in enumerate(row_keys):
        row_hash = get_hash(row_key)
        row_bin = to_bin(row_hash)
        for col_idx, col in enumerate(row_bin):
            if col == '1':
                used_squares += 1
                grid[row_idx*128+col_idx] = -1

    checked_cells = set()
    region_count = 0
    for y_idx in range(128):
        for x_idx in range(128):
            idx = y_idx*128+x_idx
            idx_val = grid[idx]
            if idx_val == -1:
                region_count += 1                
                stack = [idx]
                while stack:
                    cur_idx = stack.pop()
                    if cur_idx not in checked_cells:
                        cur_val = grid[cur_idx]
                        if cur_val == -1:
                            cur_idx_x = cur_idx % 128
                            cur_idx_y = (cur_idx - cur_idx_x) / 128
                            
                            grid[cur_idx] = region_count
                            checked_cells.add(cur_idx)
                            
                            if cur_idx_y > 0:
                                new_idx = cur_idx-128
                                stack.append(new_idx)
                            if cur_idx_y < 127:
                                new_idx = cur_idx+128
                                stack.append(new_idx)
                            if cur_idx_x > 0:
                                new_idx = cur_idx-1
                                stack.append(new_idx)
                            if cur_idx_x < 127:
                                new_idx = cur_idx+1
                                stack.append(new_idx)
    return used_squares, region_count

def check(expected, actual):    
    if actual == expected:
        print(actual, 'OK')
    else:
        print(f'{actual} != {expected} ERROR')

def main():
    input_key, outputs = open_files('day14.input', 'day14.output')
    result1, result2 = run(input_key)
    check(outputs[0], result1)
    check(outputs[1], result2)

if __name__ == '__main__':
    main()