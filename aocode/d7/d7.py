#! /usr/bin/env python3


bags_relations = open('./input.txt').read().split('\n')

SEARCH = "shiny gold"

visited = set()

tracks = {}
bg_colors = 0

for br in bags_relations:
    entry_bag = br.split('contain')[0].strip()
    inserts = br.split('contain')[1]
    insert_bag = [None] if 'no other bags' in inserts else [
        x.strip() for x in inserts.replace('.', '').split(',')]

    if entry_bag in tracks.keys():
        print(f"{entry_bag} already in tracks!")
        tracks[entry_bag] += insert_bag

    else:
        tracks[entry_bag] = insert_bag

for k, v in tracks.items():
    print(f"{k}: {v}")
    if filter(lambda x: 1 if SERACH in x else 0, v):
        bg_colors += 1

print(f"Directly: {bg_colors}")
# rzeczy
