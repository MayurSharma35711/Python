n = int(input("Test: "))
amnt = 15
def makeMore(l):
    arr = []
    for i in range(1, amnt):
        h = (l*2**i-1)/5
        if int(10*(h - int(h))) is 0:
        # this line prevents a bunch of decimals from forming
            arr.append(int(h))
    return arr

q = makeMore(n)
print(q)
# print(len(q))
l = [[0 in range(1,amnt)] for o in range(0,len(q))]
for n in range(0, len(q)):
    l[n][0] = q[n]
    l[n].append(makeMore(q[n]))
    print(l[n])

for i in range(1,35):
    q = i**3
    print(q%35)