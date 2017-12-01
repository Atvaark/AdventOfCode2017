def sum_digits(d1, d2):
    if (d1 == d2):
        return int(d1)

    return 0

def sum_neighbor(numbers):
    if len(numbers) <= 1:
        return 0
    
    sum = 0
    for i in range(0, len(numbers)):
        if i < len(numbers) - 1:
            sum += sum_digits(numbers[i], numbers[i+1])

    if len(numbers) > 2:
        sum += sum_digits(numbers[0], numbers[-1:])

    return sum

def sum_halfway(numbers):
    if len(numbers) <= 1:
        return 0
    
    if len(numbers) % 2 > 0:
        return 0

    sum = 0
    for i in range(0, len(numbers)):
        j = (int(len(numbers)/2)+i)%len(numbers)

        if i != j:
            sum += sum_digits(numbers[i], numbers[j])

    return sum

def main():
    with open('day01.input') as f:
        in_lines = f.read().splitlines()

    with open('day01.output') as f:
        out_lines = f.read().splitlines()

    for n in range(0, len(in_lines)):
        in_line = in_lines[n].split(" ")
        in_part = in_line[0]
        in_number = in_line[1]

        out_line = int(out_lines[n])

        if in_part == '1':
            actual = sum_neighbor(in_number)            
        elif in_part == '2':
            actual = sum_halfway(in_number)
        else:
            actual = -1

        match = out_line == actual
        
        print('{} {} {} {}'.format(n+1, in_part, actual, match))

if __name__ == '__main__':
    main()
