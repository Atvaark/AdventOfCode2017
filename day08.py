def open_files(input_file, output_file):
    with open(input_file) as f:
        lines = f.read().splitlines()

    instructions = []
    for line in lines:
        parts = line.split(' ')
        
        reg1 = parts[0]
        op = parts[1]
        opd1 = int(parts[2])
        ifw = parts[3]
        reg2 = parts[4]
        comp = parts[5]
        opd2 = int(parts[6])

        instruction = (reg1, op, opd1, reg2, comp, opd2)
        instructions.append(instruction)

    with open(output_file) as f:
        output_vals = list(map(int, f.read().splitlines()))

    return instructions, output_vals

def compare(opd1, opd2, comp):
    if comp == '<':
        return opd1 < opd2
    elif comp == '>':
        return opd1 > opd2
    elif comp == '>=':
        return opd1 >= opd2
    elif comp == '<=':
        return opd1 <= opd2
    elif comp == '==':
        return opd1 == opd2
    elif comp == '!=':
        return opd1 != opd2
    
    print('unknown comparator', comp)
    return False

def run_op(opd1, opd2, op):
    if op == 'inc':
        return opd1 + opd2
    elif op == 'dec':
        return opd1 - opd2

    print('unknown operation', op)
    return 0

def run(instructions):
    regs = {}
    max_regval = 0
    for instruction in instructions:
        compOpd1 = regs.get(instruction[3], 0)
        compOp = instruction[4] 
        compOpd2 = instruction[5]
        if compare(compOpd1, compOpd2, compOp):
            reg1 = instruction[0]
            opd1 = regs.get(reg1, 0)
            opd2 = instruction[2]
            op = instruction[1]
            regval = run_op(opd1, opd2, op)
            regs[reg1] = regval

            if regval > max_regval:
                max_regval = regval

    last_max_regval = 0
    for regval in regs.values():
        if regval > last_max_regval:
            last_max_regval = regval

    return last_max_regval, max_regval
    
def check(expected, actual):    
    if actual == expected:
        print(actual, 'OK')
    else:
        print(f'{actual} != {expected} ERROR')
def main():
    instructions, output_vals = open_files('day08.input', 'day08.output')
    last_max_regval, max_regval = run(instructions)

    check(output_vals[0], last_max_regval)
    check(output_vals[1], max_regval)

if __name__ == '__main__':
    main()