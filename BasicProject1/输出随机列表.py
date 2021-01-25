from random import randint, randrange

x = randint(30, 41)
print(x)
y = 0
alist = []
for _ in range(30, 41):
    while y < x:
        alist.append(randint(1, 10))
        y += 1
    y = 0
blist = alist[::-1]
clist = list(zip(alist, blist))
print(len(clist))  # 原clist长度
clist = sorted(set(clist), key=clist.index)
print(len(clist))  # 去除重复clist长度
print(clist)
dlist = []
for (m, n) in clist:
    if m < n:
        dlist.append(m + n)
print(len(dlist))
print(dlist)
