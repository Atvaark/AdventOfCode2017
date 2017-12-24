def run(components):
    max_strength = 0
    max_length = 0
    max_length_strength = 0
    for perm in run_recursive(components, 0):
        strength = get_strength(perm)
        if strength > max_strength:
            max_strength = strength

        length = len(perm)
        if length > max_length:
            max_length = length
            max_length_strength = strength
        elif length == max_length and strength > max_length_strength:
            max_length_strength = strength

    return max_strength, max_length_strength


def run_recursive(components, prev_pins):
    matches = []
    for idx, comp in enumerate(components):
        if comp[0] == prev_pins:
            matches.append((comp, idx, comp[1]))
        elif comp[1] == prev_pins:
            matches.append((comp, idx, comp[0]))
    if matches:
        for match in matches:
            comp = match[0]
            idx = match[1]
            prev_pins = match[2]
            remaining_comps = components[:idx] + components[idx+1:]
            if remaining_comps:
                for sub_match in run_recursive(remaining_comps, prev_pins):
                    yield [comp] + sub_match

            yield [comp]
    else:
        return

def get_strength(components):
    strength = 0
    for component in components:
        strength += component[0]
        strength += component[1]
    return strength

def read_inputs(input_file, output_file):
    with open(input_file) as f:
        lines = f.read().splitlines()

    components = []
    for line in lines:
        split = list(map(int, line.split('/')))

        component = (
            split[0],
            split[1]
        )
        components.append(component)

    with open(output_file) as f:
        outputs = list(map(int, f.read().splitlines()))
    return components, outputs

def check(expected, actual):    
    if actual == expected:
        print(actual, 'OK')
    else:
        print(f'{actual} != {expected} ERROR')

def main():
    components, outputs, = read_inputs('day24.input', 'day24.output')
    strength, max_length_strength = run(components)
    check(outputs[0], strength)
    check(outputs[1], max_length_strength)


if __name__ == '__main__':
    main()