#! /usr/bin/env python3


bags_relations = open('./input.txt').read().split('\n')

SEARCH = "shiny gold bag"

to_visit = set()
visited = set()
tracks = {}
bg_colors = set()

for br in bags_relations:
    entry_bag = br.split('contain')[0].strip().replace('bags', 'bag')
    inserts = br.split('contain')[1]
    insert_bag = [''] if 'no other bags' in inserts else [
        x.strip().replace('bags', 'bag') for x in inserts.replace('.', '').split(',')]
    if entry_bag in tracks.keys():
        print(f"{entry_bag} already in tracks!")
        tracks[entry_bag] += insert_bag

    else:
        tracks[entry_bag] = insert_bag

for k, v in tracks.items():
    if any(SEARCH in sub for sub in v):
        bg_colors.add(k)
        if k != '':
            to_visit.add(k)

while len(to_visit):
    bag = to_visit.pop()
    for k, v in tracks.items():
        if any(bag in sub for sub in v):
            if k not in visited:
                bg_colors.add(k)
                to_visit.add(k)

    visited.add(bag)


def count(s, m):
    if m[s] == ['']:
        return 1

    else:
        return sum(map(lambda x: int(x.split(' ', 1)[0]) * count(x.split(' ', 1)[1], m), m[s])) + 1


print(f"First: {len(bg_colors)}")
print(f"Second: {count(SEARCH, tracks) - 1}")
