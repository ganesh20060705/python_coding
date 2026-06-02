n = int(input())

s = 0
p = 1


while n > 0:
    digit = n % 10
    s += digit
    p *= digit
    n //= 10

if s == p:
    print("Spy Number")
else:
    print("Not a Spy Number")