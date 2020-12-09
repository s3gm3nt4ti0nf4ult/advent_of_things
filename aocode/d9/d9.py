#! /usr/bin/env python3

nums = [int(x) for x in open('./input.txt').read().split('\n')]
for l, u in zip(range(0, len(nums) - 25), range(25, len(nums))):
    
