import re
from copy import deepcopy

def open_files(input_file, output_file):
    with open(input_file) as f:
        lines = f.read().splitlines()

    particles = []
    for line in lines:
        matches = re.findall(r'([pva])=\<([- ]?\d+),([- ]?\d+),([- ]?\d+)\>', line)

        particle = {}
        for match in matches:
            particle[match[0]] = (
                int(match[1]),
                int(match[2]),
                int(match[3]),
            )

        particles.append(particle)

    with open(output_file) as f:
        outputs = list(map(int, f.read().splitlines()))
    return particles, outputs

def simulate_step(particle):
    a = particle['a']
    v = particle['v']
    p = particle['p']

    v = (
        v[0] + a[0],
        v[1] + a[1],
        v[2] + a[2]
    )
    particle['v'] = v

    p = (
        p[0] + v[0],
        p[1] + v[1],
        p[2] + v[2]
    )
    particle['p'] = p

def simulate(particles, iterations):
    for _ in range(iterations):
        for particle in particles:
            simulate_step(particle)
    return particles

def simulate_collisions(particles, iterations):
    for _ in range(iterations):
        for particle in particles:
            simulate_step(particle)

        positions = {}
        for idx, particle in enumerate(particles):
            position = particle['p']
            idx_list = positions.get(position, [])
            idx_list.append(idx)
            positions[position] = idx_list

        for position, idx_list in positions.items():
            if len(idx_list) > 1:
                for particle in particles[:]:
                    p = particle['p']
                    if p == position:
                        particles.remove(particle)

    return particles

def get_closest_particle(particles):
    min_manhattan = None
    min_idx = None
    for idx, particle in enumerate(particles):
        p = particle['p']
        dist = sum(map(abs, p))
        if min_manhattan is None or min_manhattan > dist:
            min_manhattan = dist
            min_idx = idx

    return min_idx, min_manhattan

def check(expected, actual):    
    if actual == expected:
        print(actual, 'OK')
    else:
        print(f'{actual} != {expected} ERROR')

def main():
    input_particles, outputs = open_files('day20.input','day20.output')

    iterations = 10000
    particles_1 = deepcopy(input_particles)
    particles_1 = simulate(particles_1, iterations)
    min_idx, _ = get_closest_particle(particles_1)
    check(outputs[0], min_idx)

    iterations = 10000
    particles_2 = deepcopy(input_particles)
    particles_2 = simulate_collisions(particles_2, iterations)
    particles_2_count = len(particles_2)
    check(outputs[1], particles_2_count)

if __name__ == '__main__':
    main()