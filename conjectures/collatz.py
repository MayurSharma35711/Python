# import matplotlib.pyplot as plot

def collatz(l):
    if int(l) % 2 is 0:
        l /= 2
    else:
        l = 5*l+1
    return int(l)

q = int(input("give number: "))


counter = 0
print(q)

while q is not 1:
    q = collatz(q)
    print(q)
    # print(counter, end ="\t")
    counter += 1
    if int(q) is 1:
        # print("here")
        break
print('steps: ', counter)