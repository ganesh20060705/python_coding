s,e=map(int, input().split())

def power_add(num, p):
    s = 0
    while num > 0:
        dig = num % 10
        s += dig ** p
        num = num // 10
    return s

for num in range(s, e + 1):
    p = len(str(num))
    if num == power_add(num, p):
        print(num)