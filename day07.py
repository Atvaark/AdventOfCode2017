def open_files(input_file, output_file):
    with open(input_file) as f:
        input_lines = f.read().splitlines()

    with open(output_file) as f:
        output_lines = f.read().splitlines()

    output = (output_lines[0], int(output_lines[1]))
    
    return input_lines, output

def check(expected, actual):    
    if actual == expected:
        print(actual, 'OK')
    else:
        print(f'{actual} != {expected} ERROR')

def parse_nodes(input_lines):
    nodes = {}
    for line in input_lines:
        line_parts = line.split(' ')        
        name = line_parts[0]
        weight = int(line_parts[1].replace('(', '').replace(')', ''))        
        child_names = []
        if len(line_parts) > 3:
            for child_name in line_parts[3:]:
                child_names.append(child_name.replace(',', ''))

        nodes[name] = (name, weight, child_names)  
    return nodes

def get_root_node(nodes):
    if len(nodes) == 0:
        return None

    current_node = list(nodes.values())[0]
    while True:
        root = True
        for node in nodes.values():
            if current_node[0] in node[2]:
                current_node = node
                root = False
                break
        if root:
            return current_node


def calc_child_weights(nodes, node):
    node_children = node[2]
    child_node_sum = 0
    prev_child_sum = None
    child_errors = {}
    child_sums = {}
    check_error = False
    fixed_node = None
    
    for child_node_name in node_children:
        c = nodes[child_node_name]
        child_weight, child_err, child_fixed_node = calc_weight(nodes, c)
        
        if fixed_node is None:
            fixed_node = child_fixed_node
        
        child_errors[child_node_name] = child_err
        child_sums[child_node_name] = child_weight
        child_node_sum += child_weight
        
        if child_err:
            check_error = True
        
        if prev_child_sum is None:
            prev_child_sum = child_weight
        else:
            if prev_child_sum != child_weight:
                check_error = True
        
    if check_error:
        any_child_errs = False
        for child_error in child_errors.values():
            any_child_errs = any_child_errs or child_error
            
        if not any_child_errs:
            # find a child with an invalid weight assuming the 
            count_dict = {}
            for k, v in child_sums.items():
                count = count_dict.get(v, 0)
                count += 1
                count_dict[v] = count
                
            max_count = 0
            max_count_val = 0
            for k, v in count_dict.items():
                if v > max_count:
                    max_count = v
                    max_count_val = k
            
            other_count_val = 0
            for k, v in count_dict.items():
                if v != max_count:
                    other_count_val = k
                    
            invalid_child_name = ''                    
            for k, v in child_sums.items():
                if v == other_count_val:
                    invalid_child_name = k
            
            # calc diff
            val_diff = max_count_val - other_count_val
            
            # find new weight
            invalid_node = nodes[invalid_child_name]                            
            tmp_node_list = list(invalid_node)
            tmp_node_list[1] = invalid_node[1] + val_diff    
            fixed_node = tuple(tmp_node_list)
        
    return child_node_sum, child_sums, check_error, fixed_node
    
def calc_weight(nodes, node):
    node_weight = node[1]
    node_children = node[2]
    
    if not node_children:
        return node_weight, False, None
        
    child_node_sum, _, check_error, fixed_node = calc_child_weights(nodes, node)
    s = node_weight + child_node_sum
    return s, check_error, fixed_node
     
def main():
    input_lines, output = open_files('day07.input', 'day07.output')
    nodes = parse_nodes(input_lines)
    root_node = get_root_node(nodes)
    root_node_name = root_node[0]
    check(output[0], root_node_name)
    
    _, _, fixed_node = calc_weight(nodes, root_node)
    fixed_node_weight = fixed_node[1]
    check(output[1], fixed_node_weight)

if __name__ == '__main__':
    main()