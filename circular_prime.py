import math
n = input()

def prime(num):
    if num < 2:
        return False

    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False

    return True

flag = True

for i in range(len(n)):
    rot = n[i:] + n[:i]

    if not prime(int(rot)):
        flag = False
        break

if flag:
    print("Circular Prime")
else:
    print("Not Circular Prime")