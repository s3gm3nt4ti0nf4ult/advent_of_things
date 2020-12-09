#! /usr/bin/env python3
from itertools import combinations


nums = [int(x) for x in open('./input3.txt').readlines() if x]
candaidates = nums[:]
for l, u in zip(range(0, len(nums) - 26), range(25, len(nums) - 1)):
    for i in combinations(nums[l:u + 1], 2):
        if sum(i) == nums[u + 1]:
            candaidates[u + 1] = None
            break

candaidates = sorted([x for x in candaidates if x][26:])[0]
print(f"First: {candaidates}")

nums = nums[:nums.index(candaidates)]
i, j = 0, 0
while j < len(nums) - 1:
    if i >= j:
        j += 1
    if sum(nums[i:j + 1]) > candaidates:
        i += 1
    elif sum(nums[i:j + 1]) < candaidates:
        j += 1

    else:
        print(f"Second: {min(nums[i:j+1]) + max(nums[i:j+1])}")
        break
