import copy

def open_files(input_file, output_file):
    with open(input_file) as f:
        lines = f.read().splitlines()

    input_map = {}
    for line in lines:
        line_vals = list(map(int, line.replace(':', '').split(' ')))
        depth = line_vals[0]
        range = line_vals[1]
        input_map[depth] = [0] * range
        input_map[depth][0] = 1

    with open(output_file) as f:
        outputs = list(map(int, f.read().splitlines()))

    return input_map, outputs

def reset_map(input_map):
    for k, v in input_map.items():
        for i in range(len(v)):
            if v[i] != 0:
                v[i] = 0
                break

        v[0] = 1

def move_scanners(input_map):
    for scan, scan_range in input_map.items():
        scan_dir = 1
        for idx_scan, val in enumerate(scan_range):
            if val == 1 or val == 2:
                idx = idx_scan
                if val == 1:
                    scan_dir = 1
                else:
                    scan_dir = 2                
                break
        
        if scan_dir == 1:
            idx_new = idx + 1
            if idx_new == len(scan_range)-1:
                scan_dir = 2
        else:
            idx_new = idx - 1
            if idx_new == 0:
                scan_dir = 1
        

        scan_range[idx] = 0
        scan_range[idx_new] = scan_dir

def run(input_map, part):
    max_depth = max(input_map.keys())
    delay = 0
    input_map_last = copy.deepcopy(input_map)
    
    while True:
        severity = 0
        caught = False
        reset_map(input_map)
        
        if delay != 0:
            input_map = copy.deepcopy(input_map_last)
            move_scanners(input_map)
            input_map_last = copy.deepcopy(input_map)
                    
        for d in range(max_depth+1):            
            if d in input_map:
                scan_range = input_map[d]
                if scan_range[0] != 0:
                    if part == 1:
                        severity += d * len(scan_range)
                    
                    if part == 2:
                        caught = True
                        break

            move_scanners(input_map)
            
        if part == 1:
            return severity, delay
        
        if part == 2:
            if not caught:
                return -1, delay
            delay += 1
        
    return

def check(expected, actual):    
    if actual == expected:
        print(actual, 'OK')
    else:
        print(f'{actual} != {expected} ERROR')

def main():
    input_map, outputs = open_files('day13.input', 'day13.output')
    result1, _ = run(input_map, 1)
    check(outputs[0], result1)
    _, result2 = run(input_map, 2)
    check(outputs[1], result2)

if __name__ == '__main__':
    main()