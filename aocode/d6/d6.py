#! /usr/bin/env python3

t = open('./input.txt').read().split('\n\n')
answer = []
answer2 = []


for g in t:
    gset = set(list(g.replace('\n', '')))
    ans = set(list(g.replace('\n', '')))
    lines = g.split('\n')
    for l in lines:
        # ans.update(list(l))
        gset = gset.intersection(list(l))
    answer.append(len(list(ans)))
    answer2.append(len(list(gset)))    

print(sum(answer))
print(sum(answer2))
