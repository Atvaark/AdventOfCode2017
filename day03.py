from typing import Optional
from math import sqrt

def check_spiral(n: int) -> (Optional[int], Optional[int]):
    if n == 0:
        return (None, None)
    
    first_sum = None
    mem = {}
    w = 0
    h = 0
    p = (0, 0) # pos
    d = (0, 0) # dir
    for i in range(n):
        i += 1

        if i == 1:
            p = (0, 0)
            d = (1, 0) # right
            w = 0
            h = 0
            s = 1
        else:
            p = (p[0] + d[0], p[1] + d[1]) # step

            if p[0] > w:
                w += 1
                d = (0, 1) # up
            elif p[1] > h:
                h += 1
                d = (-1, 0) # left
            elif p[1] <= -h:
                d = (1, 0) # right
            elif p[0] <= -w:
                d = (0, -1) # down

            s = 0
            s += mem.get((p[0]+1, p[1]), 0)
            s += mem.get((p[0]+1, p[1]+1), 0)
            s += mem.get((p[0], p[1]+1), 0)
            s += mem.get((p[0]-1, p[1]+1), 0)
            s += mem.get((p[0]-1, p[1]), 0)
            s += mem.get((p[0]-1, p[1]-1), 0)
            s += mem.get((p[0], p[1]-1), 0)
            s += mem.get((p[0]+1, p[1]-1), 0)

            if first_sum is None and s > n:
                first_sum = s

        mem[p] = s

    distance = abs(p[0]) + abs(p[1])

    return (distance, first_sum)

def check(n, expected):
    actual = check_spiral(n)

    if expected == actual:
        print(f'{n} = {actual} OK')
    else:
        print(f'{n} != {expected} ERROR (Actual: {actual})')

def main():
    check(1, (0, None))
    check(12, (3, 23))
    check(23, (2, 25))
    check(1024, (31, 1968))
    check(325489, (552, 330785))

if __name__ == '__main__':
    main()