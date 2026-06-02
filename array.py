arr = []
n=int(input())

for i in range(n):
    arr.append(int(input()))
for i in range(len(arr)):

    for j in range(len(arr) - 1):

        if arr[j] > arr[j + 1]:

            temp = arr[j]
            arr[j] = arr[j + 1]
            arr[j + 1] = temp

print(arr)