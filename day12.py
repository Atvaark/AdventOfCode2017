import re

def open_files(input_file, output_file):
    with open(input_file) as f:
        lines = f.read().splitlines()

    inputs = {}
    for line in lines:
        split = list(map(int, re.findall(r'\b\d+\b', line)))
        inputs[split[0]] = split[1:]

    with open(output_file) as f:
        outputs = list(map(int, f.read().splitlines()))

    return inputs, outputs

def count_conn(connections):
    total_connections = 0
    for conns in connections.values():
        total_connections += len(conns)
    return total_connections

def dedupe(items):
    new_items = []
    for item in items:
        if item not in new_items:
            new_items.append(item)
    return new_items

def run(inputs):
    connections = {}
    for id in inputs:
        connections[id] = []

    total_connections = count_conn(connections)
    while True:

        for id in connections:
            ids = []
            ids += [id]
            ids += connections[id]
            ids += inputs.get(id, [])
            ids = dedupe(ids)
            connections[id] = ids

            for other_id in ids:
                other_ids = connections.get(other_id, [])
                other_ids += ids
                other_ids = dedupe(other_ids)
                connections[other_id] = other_ids

        new_connections = count_conn(connections)
        if total_connections == new_connections:
            break
        else:
            total_connections = new_connections

    count = len(connections.get(0, []))

    group_index = 0
    groups = {}
    for id, ids in connections.items():
        group_ids = [id] + ids
        if id not in groups:
            group_index += 1

        for group_id in group_ids:
            groups[group_id] = group_index
    group_count = group_index

    return count, group_count

def check(expected, actual):    
    if actual == expected:
        print(actual, 'OK')
    else:
        print(f'{actual} != {expected} ERROR')


def main():
    inputs, outputs = open_files('day12.input', 'day12.output')

    count, group_count = run(inputs)

    check(outputs[0], count)
    check(outputs[1], group_count)

if __name__ == '__main__':
    main()