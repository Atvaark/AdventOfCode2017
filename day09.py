def check(expected, actual):    
    if actual == expected:
        print(actual, 'OK')
    else:
        print(f'{actual} != {expected} ERROR')

def open_files():
    with open('day09.input') as f:
        in_lines = f.read().splitlines()

    with open('day09.output') as f:
        out_lines = f.read().splitlines()
        out_vals = [(list(map(int, out_line.split(' ')))) for out_line in out_lines]
    
    return in_lines, out_vals

def get_score(in_line):
    garbage_score = 0
    groups_score = 0
    group_level = 0
    group_scores = []
    garbage_flag = False
    ignore_flag = False

    for char in in_line:
        if ignore_flag:
            ignore_flag = False
        else:
            if garbage_flag:
                if char == '!':
                    ignore_flag = True
                elif char == '>':
                    garbage_flag = False
                else:
                    garbage_score += 1
            else:
                if char == '{':
                    group_level += 1
                    group_scores.append(group_level)
                elif char == '}':
                    group_level -= 1
                    groups_score += group_scores.pop()
                elif char == '<':
                    garbage_flag = True
                elif char == '!':
                    ignore_flag = True

    return groups_score, garbage_score

def main():
    in_lines, out_vals = open_files()

    for i, in_line in enumerate(in_lines):
        out_val = out_vals[i]
        score1, score2 = get_score(in_line)
        check(out_val[0], score1)
        check(out_val[1], score2)


if __name__ == '__main__':
    main()