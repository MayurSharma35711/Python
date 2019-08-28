# this file tests for values produced by a number
def odder(l):
    if int(l) % 2 is 0 and int(l) is not 0:
        return True
    else:
        return False


def produce(q, l):
    work = True
    if q % 3 is 2:
        q = 2*q
    elif q % 3 is 1:
        q = q
    else:
        work = False
    arr = []
    if work:
        for i in range(1, l):
            p = int((q - 1) / 3)
            q = q*4
            arr.append(p)
    else:
        print("impossible")
    return arr


q = int(input("Producer: "))
print(produce(q, 10))
