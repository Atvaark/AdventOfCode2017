from collections import deque

def open_files(input_file, output_file):
    with open(input_file) as f:
        lines = f.read().splitlines()

    instructions = []
    for line in lines:
        split = line.split(' ')

        op = split[0].strip()
        reg = split[1]
        if len(split) == 3:
            opd = split[2]
        else:
            opd = None

        instructions.append((op, reg, opd))

    with open(output_file) as f:
        outputs = list(map(int, f.read().splitlines()))

    return instructions, outputs

def get_reg_or_val(registers, opd):
    if opd.isdigit():
        return int(opd)
    elif len(opd) > 0 and opd[0] == '-' and opd[1:].isdigit():
        return int(opd)
    else:
        return registers.get(opd, 0)

def part_1(instructions):
    registers = {}
    mul_count = run(instructions, registers)
    return mul_count

def part_2(instructions):
    a = 1
    b = 0
    c = 0
    d = 0
    e = 0
    f = 0
    g = 0
    h = 0

    regs = {'a': a}
    run(instructions[0:8], regs)
    a = regs['a']
    b = regs['b']
    c = regs['c']
        
    while True:
        f = 1
        d = 2
        e = 2
        while True:
            if b % d == 0:
                f = 0
            d += 1
            if d != b:
                continue
            if f == 0:
                h += 1
            if b == c:
                return(h)
            b += 17
            break


def run(instructions, registers):
    offset = 0

    mul_count = 0
    it = 0
    while offset < len(instructions):
        op, reg, opd = instructions[offset]
        jumped = False
        if op == 'set':
            registers[reg] = get_reg_or_val(registers, opd)
        elif op == 'sub':
            x = get_reg_or_val(registers, reg)
            y = get_reg_or_val(registers, opd)
            registers[reg] = x - y
        elif op == 'mul':
            x = get_reg_or_val(registers, reg)
            y = get_reg_or_val(registers, opd)
            registers[reg] = x * y
            mul_count += 1
        elif op == 'jnz':
            x = get_reg_or_val(registers, reg)
            if x != 0:
                offset += get_reg_or_val(registers, opd)
                jumped = True
        else:
            print('ERROR', op, offset)

        if not jumped:
            offset += 1

        # it += 1
        # if it % 100 == 0:
        #     print(registers)

    return mul_count


def check(expected, actual):    
    if actual == expected:
        print(actual, 'OK')
    else:
        print(f'{actual} != {expected} ERROR')
        

def main():
    instructions, outputs = open_files('day23.input', 'day23.output')
    registers = {}
    result_1 = part_1(instructions) 
    check(outputs[0], result_1)

    result_2 = part_2(instructions) 
    check(outputs[1], result_2)

if __name__ == '__main__':
    main()