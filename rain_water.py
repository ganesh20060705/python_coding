n = int(input())

a = list(map(int, input().split()))

water = 0

for i in range(1, n - 1):

    l_max = max(a[:i+1])
    r_max = max(a[i:])

    water += min(l_max, r_max) - a[i]

print(water)