def factorial(n):
    fact = 1

    for i in range(1, n + 1):
        fact *= i

    return fact


num = int(input())

temp = num
s = 0

while temp > 0:
    digit = temp % 10
    s += factorial(digit)
    temp //= 10

if s == num:
    print("Peterson Number")
else:
    print("Not Peterson Number")