n = int(input())
arr = list(map(int, input().split()))

mx = arr[0]

for i in arr:
    if i > mx:
        mx = i

print(mx)