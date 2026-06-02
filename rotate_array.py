arr = []
n = int(input())
for i in range(n):
    arr.append(int(input()))

first = arr[0]

for i in range(len(arr) - 1):
    arr[i] = arr[i + 1]

arr[len(arr) - 1] = first

print(arr)