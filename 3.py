n = int(input())
arr = list(map(int, input().split()))

mn = arr[0]

for i in arr:
    if i < mn:
        mn = i

print(mn)