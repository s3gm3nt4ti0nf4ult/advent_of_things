#! /usr/bin/env python3
from math import prod

mapa = open('./input.txt').read().split('\n')

def slope(r, d):
    x, y = 0, 0
    tree = 0
    while y < len(mapa) - 1:
        x += r
        y += d
        if mapa[y][x % len(mapa[0])] == '#':
            tree += 1

    return tree


print(f"First: {slope(3, 1)}")
print(f"Second: {prod([slope(1, 1), slope(3, 1), slope(5, 1), slope(7, 1), slope(1, 2)]) }")
