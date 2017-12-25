import re

class State:
    def __init__(self):
        self.state = None
        self.instrs = {}

class Instruction:
    def __init__(self):
        self.ifvalue = None
        self.write = None
        self.move = None
        self.next_state = None

def open_files(input_file, output_file):
    with open(input_file) as f:
        lines = f.read().splitlines()
        start_state = None
        checksum_steps = None
        states = {}

        current_state = None       
        current_instruction = None 
        for line in lines:
            begin_match = re.search(r'Begin in state (.*)\.', line)
            if begin_match:
                start_state = begin_match.group(1)
                continue

            checksum_match = re.search(r'Perform a diagnostic checksum after (\d+) steps.', line)
            if checksum_match:
                checksum_steps = int(checksum_match.group(1))
                continue

            state_match = re.search(r'In state (.*):', line)
            if state_match:
                current_state = State()
                current_state.state = state_match.group(1)
                states[current_state.state] = current_state
                continue

            if_match = re.search(r'If the current value is (\d+)\:', line)
            if if_match:
                current_instruction = Instruction()
                current_instruction.ifvalue = int(if_match.group(1))
                current_state.instrs[current_instruction.ifvalue] = current_instruction
                continue

            write_match = re.search(r'Write the value (\d+)\.', line)
            if write_match:
                current_instruction.write = int(write_match.group(1))
                continue

            move_match = re.search(r'Move one slot to the (.*)\.', line)
            if move_match:
                move = move_match.group(1)
                if move == 'right':
                    current_instruction.move = 1
                elif move == 'left':
                    current_instruction.move = -1
                continue

            continue_match = re.search(r'Continue with state (.*)\.', line)
            if continue_match:
                current_instruction.next_state =  continue_match.group(1)
                continue
           
    with open(output_file) as f:
        output = int(f.read())

    return start_state, checksum_steps, states, output

def run(start_state, checksum_steps, states):
    current_state = start_state
    current_pos = 0
    tape = {}
    for _ in range(checksum_steps):
        tape_val = tape.get(current_pos, 0)
        state = states[current_state]
        instruction = state.instrs[tape_val]
        tape[current_pos] = instruction.write
        current_pos += instruction.move
        current_state = instruction.next_state

    checksum = 0
    for tape_val in tape.values():
        checksum += tape_val

    return checksum

def check(expected, actual):    
    if actual == expected:
        print(actual, 'OK')
    else:
        print(f'{actual} != {expected} ERROR')

def main():
    start_state, checksum_steps, states, output = open_files('day25.input', 'day25.output')
    checksum = run(start_state, checksum_steps, states)
    check(output, checksum)

if __name__ == '__main__':
    main()