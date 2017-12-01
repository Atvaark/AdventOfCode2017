def sum_digits(d1, d2):
    if (d1 == d2):
        return int(d1)

    return 0

def sum_input(input):
    if len(input) <= 1:
        return 0
    
    sum = 0
    for i in range(0, len(input)):
        if i < len(input) - 1:
            sum += sum_digits(input[i], input[i+1])

    if len(input) > 2:
        sum += sum_digits(input[0], input[-1:])

    return sum

def main():
    with open('day01.input') as f:
        in_lines = f.read().splitlines()

    with open('day01.output') as f:
        out_lines = f.read().splitlines()

    for n in range(0, len(in_lines)):
        in_line = in_lines[n]
        out_line = int(out_lines[n])

        actual = sum_input(in_line)

        match = out_line == actual

        print (match)

if __name__ == '__main__':
    main()
