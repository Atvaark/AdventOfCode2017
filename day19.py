def open_files(input_file, output_file):
    with open(input_file) as f:
        lines = f.read().splitlines()

        grid = []
        for line in lines:
            row = []
            for cell in line:
                row.append(cell)
            grid.append(row)
    
    with open(output_file) as f:
        lines = f.read().splitlines()
        outputs = (
            lines[0],
            int(lines[1])
        )
    
    return grid, outputs

def print_grid(grid):
    for row in grid:
        for cell in row:
            print(cell, end='')
        print()

def run(grid):
    for idx, cell in enumerate(grid[0]):
        if cell == '|':
            pos = (idx, 0)
            direction = (0, 1)
            break

    path = ''
    steps = 0
    while True:
        cell = grid[pos[1]][pos[0]]
        if cell == '|':
            pos = (pos[0]+direction[0], pos[1]+direction[1])
            steps += 1
        elif cell == '+':
            prev_pos = (pos[0]-direction[0], pos[1]-direction[1])
            other_pos_list = [
                (pos[0], pos[1]-1, [' ', '-']), # up | +
                (pos[0], pos[1]+1, [' ', '-']), # down | +
                (pos[0]-1, pos[1], [' ', '|']), # left - +
                (pos[0]+1, pos[1], [' ', '|'])  # right - +
            ]

            found_other_pos = None
            for other_pos in other_pos_list:
                if other_pos[0] == prev_pos[0] and other_pos[1] == prev_pos[1]:
                    continue

                if other_pos[0] < 0 or other_pos[0] >= len(grid[0]):
                    continue

                if other_pos[1] < 0 or other_pos[1]>= len(grid):
                    continue

                invalid_cells = other_pos[2]
                other_cell = grid[other_pos[1]][other_pos[0]]
                if other_cell in invalid_cells:
                    continue

                if other_cell == 'L':
                    pass

                found_other_pos = (other_pos[0], other_pos[1])
                break
          
            if found_other_pos is None:
                break

            direction = (
                found_other_pos[0] - pos[0],
                found_other_pos[1] - pos[1],
            )
            pos = (pos[0]+direction[0], pos[1]+direction[1])
            steps += 1
        elif cell == '-':
            pos = (pos[0]+direction[0], pos[1]+direction[1])
            steps += 1
        elif cell == ' ':
            break
        else:
            path += cell
            pos = (pos[0]+direction[0], pos[1]+direction[1])
            steps += 1

    return path, steps

def check(expected, actual):    
    if actual == expected:
        print(actual, 'OK')
    else:
        print(f'{actual} != {expected} ERROR')

def main():
    grid, outputs = open_files('day19.input', 'day19.output')
    path, steps = run(grid)

    check(outputs[0], path)
    check(outputs[1], steps)

if __name__ == '__main__':
    main()