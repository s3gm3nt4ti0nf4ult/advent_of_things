#! /usr/bin/env python3

from itertools import groupby
from operator import itemgetter


bpass = open('./input.txt').read().split('\n')


def bisection(val, m='col'):
    val = list(val)
    start = [0, 128] if m == 'row' else [0, 8]
    while val:
        tmp = val.pop(0)
        if tmp == 'F':
            start[1] = (start[0] + start[1]) // 2
        elif tmp == 'B':
            start[0] = (start[0] + start[1]) // 2 

        elif tmp == 'L':
            start[1] = (start[0] + start[1]) // 2
        elif tmp == 'R':
           start[0] = (start[0] + start[1]) // 2 
    # print(sum(start) // 2)
    return sum(start) // 2

def seat_id(val):
    return bisection(val[:7], 'row') * 8 + bisection(val[7:], 'col')


p = sorted(list(map(seat_id, bpass)))
d = set(range(min(p), max(p) + 1))
present = set()
print(f"First {max(p)}")
for k, g in groupby(enumerate(p), lambda ix: ix[0] - ix[1]):
    present.update(list(map(itemgetter(1), g)))
print(f"Second: {d.difference(present).pop()}")
# print(seat_id('FBFBBFFRLR'))