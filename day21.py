from __future__ import print_function
from copy import deepcopy
import re

def open_files(input_file, output_file):
    with open(input_file) as f:
        input_lines = f.read().splitlines()

    input_rules = []
    for line in input_lines:
        m = re.match(r'^(.*) =\> (.*)$', line)
        if m:
            g = m.groups()
            left = g[0]
            left_lines = left.split('/')
            left_rule = list(map(list, left_lines))

            right = g[1]
            right_line = right.split('/')
            right_rule = list(map(list, right_line))
            rule = (
                left_rule,
                right_rule
            )

            input_rules.append(rule)

    with open(output_file) as f:
        outputs = list(map(int, f.read().splitlines()))

    return input_rules, outputs

def rect_maches(rect1, rect2):
    for y in range(len(rect1)):
        row1 = rect1[y]
        row2 = rect2[y]

        for x in range(len(row1)):
            if row1[x] != row2[x]:
                return False
                
    return True
    
def rot(rect, n):
    new_rect = deepcopy(rect)
    
    for _ in range(n):
        new_rect = list(zip(*new_rect))[::-1]
        
    return new_rect
    
def flip_vert(rect):
    new_rect = deepcopy(rect)
    
    for y, row in enumerate(rect):
        for x, cell in enumerate(row):
            new_rect[y][len(row)-x-1] = cell
    
    return new_rect
    
def flip_hor(rect):
    new_rect = deepcopy(rect)

    for y, row in enumerate(rect):
        for x, cell in enumerate(row):
            new_rect[len(rect)-y-1][x] = cell

    return new_rect
    
def find_match(image_rect, rules):

    for rule in rules:
        rule_rec = rule[0]
        if len(rule_rec) != len(image_rect):
            continue
    
        if (rect_maches(image_rect, rule_rec) or # normal
            rect_maches(flip_vert(image_rect), rule_rec) or # flip v
            rect_maches(flip_hor(image_rect), rule_rec) or # flip h
            rect_maches(rot(image_rect, 1), rule_rec) or # rot 1
            rect_maches(rot(image_rect, 2), rule_rec) or # rot 2
            rect_maches(rot(image_rect, 3), rule_rec) or # rot 3
            rect_maches(rot(flip_vert(image_rect), 1), rule_rec) or # rot 1 flip v
            rect_maches(rot(flip_vert(image_rect), 2), rule_rec) or # rot 2 flip v
            rect_maches(rot(flip_vert(image_rect), 3), rule_rec) or # rot 3 flip v
            rect_maches(rot(flip_hor(image_rect), 1), rule_rec)  or # rot 1 flip h
            rect_maches(rot(flip_hor(image_rect), 2), rule_rec)  or # rot 2 flip h
            rect_maches(rot(flip_hor(image_rect), 3), rule_rec)     # rot 3 flip h
            ):
            return rule[1]
            
    return None

def replace_image(image, rules, size, block_size):
    blocks_count = int(size/block_size)
    block_size_new = block_size + 1
    size_new =  blocks_count * block_size_new

    image_new = []
    for _ in range(size_new):
        row = ['.'] * size_new
        image_new.append(row)

    for y_block in range(blocks_count):
        for x_block in range(blocks_count):
            x_offset = x_block * block_size
            y_offset = y_block * block_size

            # cut image block
            img_rect = []
            
            for y in range(y_offset, y_offset+block_size):
                img_row = image[y][x_offset:x_offset+block_size]
                img_rect.append(img_row)

            # find first matching rule in block
            match = find_match(img_rect, rules)
            if match is None:
                
                continue
            else:
                x_offset_new = x_block * block_size_new
                y_offset_new = y_block * block_size_new
                
                for row_idx, row in enumerate(match):
                    image_new_row = image_new[y_offset_new+row_idx]
                    image_new_row = image_new_row[:x_offset_new] + row + image_new_row[x_offset_new+block_size_new:]
                    image_new[y_offset_new+row_idx] = image_new_row

    return image_new

def run(image, rules, iterations):
    for it in range(iterations):
        size = len(image[0])

        if size % 2 == 0:
            image = replace_image(image, rules, size, 2)
        elif size % 3 == 0:
            image = replace_image(image, rules, size, 3)

    pixel_count = 0
    for row in image:
        for cell in row:
            if cell == '#':
                pixel_count += 1

    return pixel_count

def check(expected, actual):    
    if actual == expected:
        print(actual, 'OK')
    else:
        print(f'{actual} != {expected} ERROR')

def main():    
    input_rules, outputs = open_files('day21.input', 'day21.output')
    input_image = [
        ['.', '#', '.'],
        ['.', '.', '#'],
        ['#', '#', '#'],
    ]
    pixel_count_1 = run(input_image, input_rules, 5)
    check(outputs[0], pixel_count_1)

    input_image = [
        ['.', '#', '.'],
        ['.', '.', '#'],
        ['#', '#', '#'],
    ]
    pixel_count_2 = run(input_image, input_rules, 18)
    check(outputs[1], pixel_count_2)

if __name__ == '__main__':
    main()