# /usr/bin/env python

acc = 0
acc2 = 0
passwd = open("./input2.txt").read().split("\n")
for i in passwd:
    if not i:
        continue
    rep, let, p = i.split(" ")
    rep = list(map(lambda x: int(x), rep.split("-")))
    let = let.replace(":", "")
    if rep[0] <= p.count(let) <= rep[1]:
        acc += 1

    try:
        if (p[rep[0] - 1] == let or p[rep[1] - 1] == let) and p[rep[0] - 1] != p[
            rep[1] - 1
        ]:
            acc2 += 1
    except IndexError as e:
        print(e)
print(acc)
print(acc2)
