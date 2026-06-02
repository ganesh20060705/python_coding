n = int(input())
arr = list(map(int, input().split()))

copy_arr = []

for i in arr:
    copy_arr.append(i)

for i in copy_arr:
    print(i, end=" ")