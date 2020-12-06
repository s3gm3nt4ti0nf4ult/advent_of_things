#! /usr/bin/env python3
from functools import reduce
from itertools import product

# part 1
num = sorted(
    list(
        map(
            lambda x: int(x),
            filter(lambda x: x != "", open("./input1.txt").read().split("\n")),
        )
    )
)
i, j, sol = 0, len(num) - 1, []
while i <= j:
    prod = num[i] + num[j]

    if prod == 2020:
        sol = [num[i], num[j]]
        i += 1
        j -= 1

    if prod < 2020:
        i += 1

    else:
        j -= 1

print(f"Part1: {sol}: {reduce((lambda x, y: x*y), sol)}")

# part 2
sol = []
set_num = set(num)  # in operation O(1)
for i, j in product(num, num):
    left = 2020 - (i + j)
    if left <= 0:
        continue
    elif left in set_num:
        sol = [i, j, left]
        break
print(f"Part2: {sol}: {reduce((lambda x,y: x*y), sol)}")
