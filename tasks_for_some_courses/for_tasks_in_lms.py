s = input()
s1 = input()
station = s.split()
ix = s1.split()
g = 0
ix = [int(i) - 1 for i in ix]
station = [int(st) for st in station]
for i in range(ix[0] + 1, ix[1] + 1):
    g += station[i]
print(g)
