q = input("Enter a number: ")

p = 3*int(q)+1


def odd(n):
    if int(n) % 2 is 1:
        return True
    else:
        return False


for i in range(1, 10):
    test = int(p)/2**i
    if odd(test):
        print(int(test))
        break
