def open_input(path):
    with open(path) as f:
        rows_raw = f.read().splitlines()

    rows = []
    for row in rows_raw:
        columns_raw = row.split()

        columns = []
        for column in columns_raw:
            n = int(column)
            columns.append(n)

        rows.append(columns)

    return rows

def open_output(path):
    with open('day02.output') as f:
        lines = f.read().splitlines()

    vals = []
    for line in lines:
        vals.append(int(line))
    return vals

def calc_checksum_sum(matrix):
    diffsum = 0
    for row in matrix:
        min_col = None
        max_col = None
        for column in row:
            if min_col is None or min_col > column:
                min_col = column

            if max_col is None or max_col < column:
                max_col = column
        
        diff = max_col-min_col
        diffsum += diff

    return diffsum

def calc_checksum_div(matrix):
    divsum = 0
    for row in matrix:
        for idx, column in enumerate(row):
            for other_column in row[idx+1:]:                
                max_col = max(column, other_column)
                min_col = min(column, other_column)

                if max_col % min_col == 0:
                    divsum += int(max_col/min_col)

    return divsum

def main():
    input_matrix = open_input('day02.input')
    output_values = open_output('day02.output')

    checksum1 = calc_checksum_sum(input_matrix)
    expected1 = output_values[0]
    match1 = checksum1 == expected1
    print(match1)

    checksum2 = calc_checksum_div(input_matrix)
    expected2 = output_values[1]
    match2 = checksum2 == expected2
    print(match2)

if __name__ == '__main__':
    main()