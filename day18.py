from collections import deque

def open_files(input_file, output_file):
    with open(input_file) as f:
        lines = f.read().splitlines()

    instructions = []
    for line in lines:
        split = line.split(' ')

        op = split[0]
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
    offset = 0

    last_rcv_freq = None
    last_sound_freq = None

    registers = {}
    while offset < len(instructions):
        op, reg, opd = instructions[offset]
        jumped = False
        if op == 'snd':
            x = get_reg_or_val(registers, reg)
            last_sound_freq = x
        elif op == 'set':
            registers[reg] = get_reg_or_val(registers, opd)
        elif op == 'add':
            x = get_reg_or_val(registers, reg)
            y = get_reg_or_val(registers, opd)
            registers[reg] = x + y
        elif op == 'mul':
            x = get_reg_or_val(registers, reg)
            y = get_reg_or_val(registers, opd)
            registers[reg] = x * y
        elif op == 'mod':
            x = get_reg_or_val(registers, reg)
            y = get_reg_or_val(registers, opd)
            registers[reg] = x % y
        elif op == 'rcv':
            x = get_reg_or_val(registers, reg)
            if x != 0:
                last_rcv_freq = last_sound_freq
                break
        elif op == 'jgz':
            x = get_reg_or_val(registers, reg)
            if x > 0:
                offset += get_reg_or_val(registers, opd)
                jumped = True
        else:
            print('ERROR', op)

        if not jumped:
            offset += 1

    return last_rcv_freq

def part_2(instructions):
    regs_1 = {'p': 0}
    regs_2 = {'p': 1}

    offset_1 = 0
    offset_2 = 0

    done_1 = False
    done_2 = False

    queue_1 = deque()
    queue_2 = deque()

    send_count = 0

    wait_1 = False
    wait_2 = False

    send_count_1 = 0
    send_count_2 = 0
    while not done_1 or not done_2:
        while not done_1 and not wait_1:
            offset_1, done_1, wait_1, send_count_1 = part_2_run(
                0,
                instructions,
                offset_1,
                regs_1,
                queue_2,
                queue_1)
            send_count += send_count_1

            if wait_2 and send_count_1 > 0:
                wait_2 = False

        while not done_2 and not wait_2:
            offset_2, done_2, wait_2, send_count_2 = part_2_run(
                1,
                instructions,
                offset_2,
                regs_2,
                queue_1,
                queue_2)

            if wait_1 and send_count_2 > 0:
                wait_1 = False

        if (send_count_1 == 0 and send_count_2 == 0 and wait_1 and wait_2) or (wait_1 and done_2) or (wait_2 and done_1):
            break

    return send_count


def part_2_run(pid, instructions, offset, registers, rcv_queue, snd_queue):
    op, reg, opd = instructions[offset]
    jumped = False
    send_count = 0
    waiting = False
    if op == 'snd':
        x = get_reg_or_val(registers, reg)
        snd_queue.append(x)
        send_count += 1
    elif op == 'set':
        registers[reg] = get_reg_or_val(registers, opd)
    elif op == 'add':
        x = get_reg_or_val(registers, reg)
        y = get_reg_or_val(registers, opd)
        registers[reg] = x + y
    elif op == 'mul':
        x = get_reg_or_val(registers, reg)
        y = get_reg_or_val(registers, opd)
        registers[reg] = x * y
    elif op == 'mod':
        x = get_reg_or_val(registers, reg)
        y = get_reg_or_val(registers, opd)
        registers[reg] = x % y
    elif op == 'rcv':
        if rcv_queue:
            x = rcv_queue.popleft()
            registers[reg] = x
        else:
            jumped = True
            waiting = True
    elif op == 'jgz':
        x = get_reg_or_val(registers, reg)
        if x > 0:
            offset += get_reg_or_val(registers, opd)
            jumped = True
    else:
        print('ERROR', op)

    if not jumped:
        offset += 1

    return offset, offset >= len(instructions), waiting, send_count

def check(expected, actual):    
    if actual == expected:
        print(actual, 'OK')
    else:
        print(f'{actual} != {expected} ERROR')
        

def main():
    instructions, outputs = open_files('day18.input', 'day18.output')
    result_1 = part_1(instructions) 
    check(outputs[0], result_1)

    result_2 = part_2(instructions) 
    check(outputs[1], result_2)

if __name__ == '__main__':
    main()